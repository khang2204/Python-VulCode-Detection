def get_records_by_time(start_time, end_time, jurisdiction, limit, offset,...
matched_hmis_table = generate_matched_table_name(jurisdiction,
    'hmis_service_stays')
matched_bookings_table = generate_matched_table_name(jurisdiction,
    'jail_bookings')
hmis_exists = table_exists(matched_hmis_table, db.engine)
bookings_exists = table_exists(matched_bookings_table, db.engine)
if not hmis_exists:
if not bookings_exists:
columns = [('matched_id', 'matched_id'), (
    'coalesce(hmis_summary.first_name, jail_summary.first_name)',
    'first_name'), (
    'coalesce(hmis_summary.last_name, jail_summary.last_name)', 'last_name'
    ), ('hmis_summary.hmis_id', 'hmis_id'), ('hmis_summary.hmis_contact',
    'hmis_contact'), ('hmis_summary.last_hmis_contact', 'last_hmis_contact'
    ), ('hmis_summary.cumu_hmis_days', 'cumu_hmis_days'), (
    'jail_summary.jail_id', 'jail_id'), ('jail_summary.jail_contact',
    'jail_contact'), ('jail_summary.last_jail_contact', 'last_jail_contact'
    ), ('jail_summary.cumu_jail_days', 'cumu_jail_days'), (
    'coalesce(hmis_summary.hmis_contact, 0) + coalesce(jail_summary.jail_contact, 0)'
    , 'total_contact')]
if not any(order_column for expression, alias in columns):
base_query = (
    """WITH hmis_summary AS (
        SELECT
            matched_id,
            string_agg(distinct internal_person_id::text, ',') as hmis_id,
            sum(
                case when client_location_end_date is not null 
                    then date_part('day', client_location_end_date::timestamp - client_location_start_date::timestamp)                     else date_part('day', updated_ts::timestamp - client_location_start_date::timestamp) 
                end
            )::int as cumu_hmis_days,
            count(*) AS hmis_contact,
            to_char(max(client_location_start_date::timestamp), 'YYYY-MM-DD') as last_hmis_contact,
            max(first_name) as first_name,
            max(last_name) as last_name
        FROM (
            SELECT
               *
            FROM {hmis_table}
            WHERE
                not (client_location_start_date < %(start_date)s AND client_location_end_date < %(start_date)s) and
                not (client_location_start_date > %(end_date)s AND client_location_end_date > %(end_date)s)
        ) AS hmis
        GROUP BY matched_id
    ), jail_summary AS (
        SELECT
            matched_id,
            string_agg(distinct coalesce(internal_person_id, inmate_number)::text, ',') as jail_id,
            sum(
                case when jail_exit_date is not null 
                    then date_part('day', jail_exit_date::timestamp - jail_entry_date::timestamp)                     else date_part('day', updated_ts::timestamp - jail_entry_date::timestamp) 
                end
            )::int as cumu_jail_days,
            count(*) AS jail_contact,
            to_char(max(jail_entry_date::timestamp), 'YYYY-MM-DD') as last_jail_contact,
            max(first_name) as first_name,
            max(last_name) as last_name
        FROM (
            SELECT
               *
            FROM {booking_table}
            WHERE
                not (jail_entry_date < %(start_date)s AND jail_exit_date < %(start_date)s) and
                not (jail_entry_date > %(end_date)s AND jail_exit_date > %(end_date)s)
        ) AS jail
        GROUP BY matched_id
    )
    SELECT
    {columns}
    FROM hmis_summary
    FULL OUTER JOIN jail_summary USING(matched_id)
    """
    .format(hmis_table=matched_hmis_table, booking_table=
    matched_bookings_table, columns=',\n'.join('{} as {}'.format(expression,
    alias) for expression, alias in columns)))
logging.info('Querying table records')
if order not in {'asc', 'desc'}:
if not isinstance(limit, int) and not limit.isdigit() and limit != 'ALL':
filter_by_status = {'Jail': 'jail_summary.matched_id is not null', 'HMIS':
    'hmis_summary.matched_id is not null', 'Intersection':
    'hmis_summary.matched_id = jail_summary.matched_id'}
status_filter = filter_by_status.get(set_status, 'true')
rows_to_show = [dict(row) for row in db.engine.execute(
    """
        {}
        where {}
        order by {} {}
        limit {} offset %(offset)s"""
    .format(base_query, status_filter, order_column, order, limit),
    start_date=start_time, end_date=end_time, offset=offset)]
query = """
    SELECT
    *,
    DATE_PART('day', {exit}::timestamp - {start}::timestamp) as days
    FROM {table_name}
    WHERE
        not ({start} < %(start_time)s AND {exit} < %(start_time)s) and
        not ({start} > %(end_time)s AND {exit} > %(end_time)s)
    """
hmis_query = query.format(table_name=matched_hmis_table, start=
    'client_location_start_date', exit='client_location_end_date')
bookings_query = query.format(table_name=matched_bookings_table, start=
    'jail_entry_date', exit='jail_exit_date')
logging.info('Done querying table records')
logging.info('Querying venn diagram stats')
venn_diagram_stats = next(db.engine.execute(
    """select
        count(distinct(hmis.matched_id)) as hmis_size,
        count(distinct(bookings.matched_id)) as bookings_size,
        count(distinct(case when hmis.matched_id = bookings.matched_id then hmis.matched_id else null end)) as shared_size,
        count(distinct(matched_id))
        from ({}) hmis
        full outer join ({}) bookings using (matched_id)
    """
    .format(hmis_query, bookings_query), start_time=start_time, end_time=
    end_time))
counts_by_status = {'HMIS': venn_diagram_stats[0], 'Jail':
    venn_diagram_stats[1], 'Intersection': venn_diagram_stats[2]}
logging.info('Done querying venn diagram stats')
venn_diagram_data = [{'sets': ['Jail'], 'size': venn_diagram_stats[1]}, {
    'sets': ['Homeless'], 'size': venn_diagram_stats[0]}, {'sets': ['Jail',
    'Homeless'], 'size': venn_diagram_stats[2]}]
logging.info('Retrieving bar data from database')
filtered_data = retrieve_bar_data(matched_hmis_table,
    matched_bookings_table, start_time, end_time)
logging.info('Done retrieving bar data from database')
filtered_data['tableData'] = rows_to_show
return {'vennDiagramData': venn_diagram_data, 'totalTableRows':
    counts_by_status.get(set_status, venn_diagram_stats[3]), 'filteredData':
    filtered_data}
