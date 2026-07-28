def get_inf_details(inf_file):...
"""docstring"""
data = {key: val for line in infFileLines for key, val in (line.strip().
    split('='),)}
files = [open(picture, 'rb').read() for picture in data['imageCsv'].split(',')]
return [data, files]
