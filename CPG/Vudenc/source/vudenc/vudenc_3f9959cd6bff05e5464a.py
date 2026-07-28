@tornado.gen.coroutine...
sql = (
    'INSERT INTO reports VALUES (NULL, STR_TO_DATE(%s, %s), %s, %s, %s, %s, %s, STR_TO_DATE(%s, %s), %s, %s, %s, %s, %s, %s, %s)'
    )
params = get_safe_val(src, 'date'), '%d.%m.%Y', get_safe_val(src,
    'temp_average_air'), get_safe_val(src, 'temp_average_water'), get_safe_val(
    src, 'expected_temp_air_day'), get_safe_val(src, 'expected_temp_air_night'
    ), get_safe_val(src, 'expected_temp_air_all_day'), get_safe_val(src,
    'forecast_date'), '%d.%m.%Y', get_safe_val(src, 'forecast_weather'
    ), get_safe_val(src, 'forecast_direction'), get_safe_val(src,
    'forecast_speed'), get_safe_val(src, 'forecast_temp_day_from'
    ), get_safe_val(src, 'forecast_temp_day_to'), get_safe_val(src,
    'forecast_temp_night_from'), get_safe_val(src, 'forecast_temp_night_to')
yield tx.execute(query=sql, params=params)
