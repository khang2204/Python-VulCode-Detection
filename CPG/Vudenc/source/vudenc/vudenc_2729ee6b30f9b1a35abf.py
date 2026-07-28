@classmethod...
text_query_str = str(text_query)
sql_query = "UPPER(tag.name) LIKE UPPER('%%%s%%')" % text_query_str
return self.select(sql_query)
