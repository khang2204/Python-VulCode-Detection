def _user_keywords_changed(thesis, user_request_keywords):...
db_keywords_info = {}
for kw in thesis.keywords.all():
db_keywords_info[str(kw.id)] = kw
unsorted_user_keywords = []
for kw in user_request_keywords:
if kw in db_keywords_info:
db_keywords = sorted([kw.text for kw in db_keywords_info.values()])
unsorted_user_keywords.append(db_keywords_info[kw].text)
unsorted_user_keywords.append(kw)
user_keywords = sorted([kw.split(ID_VAL_SEPARATOR)[-1] for kw in
    unsorted_user_keywords])
if user_keywords and user_keywords != db_keywords:
return True
return False
