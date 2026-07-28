def get_show_stoper_days():...
"""docstring"""
cmd = """SELECT to_char(date, 'FMMonth DD, YYYY') as date,
             ROUND(error_percent, 2) as error_rate
             FROM(
             SELECT time::date AS date,
             100 * (COUNT(*) FILTER (WHERE status = '404 NOT FOUND') /
             COUNT(*)::numeric) AS error_percent
             FROM log GROUP BY time::date) a
             WHERE error_percent > 1"""
return execute_query(cmd)
