def retrieve_bar_data(matched_hmis_table, matched_bookings_table,...
query = """
    SELECT
    *,
    DATE_PART('day', {exit}::timestamp - {start}::timestamp) as days
    FROM {table_name}
    WHERE
        not ({start} < %(start_time)s AND {exit} < %(start_time)s) and
        not ({start} > %(end_time)s AND {exit} > %(end_time)s)
    """
filtered_hmis = pd.read_sql(query.format(table_name=matched_hmis_table,
    start='client_location_start_date', exit='client_location_end_date'),
    con=db.engine, params={'start_time': start_time, 'end_time': end_time})
filtered_bookings = pd.read_sql(query.format(table_name=
    matched_bookings_table, start='jail_entry_date', exit='jail_exit_date'),
    con=db.engine, params={'start_time': start_time, 'end_time': end_time})
shared_ids = filtered_hmis[filtered_hmis.matched_id.isin(filtered_bookings.
    matched_id)].matched_id.unique()
if len(shared_ids) == 0:
logger.warning('No matched between two services')
bar_data = {'jailDurationBarData': get_histogram_bar_chart_data(
    filtered_bookings, get_days_distribution, shared_ids, 'Jail'),
    'homelessDurationBarData': get_histogram_bar_chart_data(filtered_hmis,
    get_days_distribution, shared_ids, 'Homeless'), 'jailContactBarData':
    get_histogram_bar_chart_data(filtered_bookings, get_contact_dist,
    shared_ids, 'Jail'), 'homelessContactBarData':
    get_histogram_bar_chart_data(filtered_hmis, get_contact_dist,
    shared_ids, 'Homeless')}
return bar_data
