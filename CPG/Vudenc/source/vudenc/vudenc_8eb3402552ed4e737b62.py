def get_articles_for_object(object, article_qs=None):...
if article_qs is None:
article_qs = ALL_ARTICLES
return article_qs.filter(content_type=get_ct(object), object_id=object.id)
