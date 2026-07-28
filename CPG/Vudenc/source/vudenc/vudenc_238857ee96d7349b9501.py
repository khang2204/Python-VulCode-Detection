def str_to_datetime(str):...
if not str or str == 'None':
str = datetime.today().strftime('%Y-%m-%d')
str = str[:10]
return datetime.strptime(str, '%Y-%m-%d')
