def search_date(self, string):...
search_date_result = re.search('\\d{2}.\\d{2}.\\d{4}', string)
if search_date_result:
date = search_date_result.group()
return date
