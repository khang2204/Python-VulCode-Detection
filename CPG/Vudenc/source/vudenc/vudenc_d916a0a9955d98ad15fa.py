def prettify_rows(self, rows):...
str_builder = ['\n']
for row in rows:
str_builder.append('When: {}'.format(prettify_date(row[0])))
return '\n'.join(str_builder)
str_builder.extend(row[1:])
str_builder.append('')
