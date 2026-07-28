def get_articles_by_group(article_qs, group_slug=None, group_slug_field=...
group = None
if group_slug is not None:
group = get_object_or_404(group_qs, **{group_slug_field: group_slug})
return article_qs, group
article_qs = article_qs.filter(content_type=get_ct(group), object_id=group.id)
