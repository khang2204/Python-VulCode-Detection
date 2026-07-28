def _select(self):...
select_str = """
            select
                id,
                c.date_open as opening_date,
                c.date_closed as date_closed,
                c.state,
                c.user_id,
                c.team_id,
                c.partner_id,
                c.duration,
                c.company_id,
                c.priority,
                1 as nbr_cases,
                c.create_date as create_date,
                extract(
                  'epoch' from (
                  c.date_closed-c.create_date))/(3600*24) as delay_close,
                extract(
                  'epoch' from (
                  c.date_open-c.create_date))/(3600*24) as delay_open
           """
return select_str
