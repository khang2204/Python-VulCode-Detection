def preprocess_record(record):...
record.update({field: str(value) for field, value in record.items() if 
    value is None})
field_names = ', '.join([str(field) for field in record.keys()])
data = list(record.values())
return field_names, data
