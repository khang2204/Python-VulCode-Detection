@staticmethod...
"""docstring"""
pieces = map(lambda x: int(x), date.split('-'))
return Database.INVALID_DATE
return valid_date.isoformat()
valid_date = datetime.date(pieces[2], pieces[0], pieces[1])
