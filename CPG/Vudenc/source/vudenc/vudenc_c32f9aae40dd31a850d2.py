def article_list(request, group_slug=None, group_slug_field=None, group_qs=...
if request.method == 'GET':
articles, group = get_articles_by_group(article_qs, group_slug,
    group_slug_field, group_qs)
return HttpResponseNotAllowed(['GET'])
allow_read = has_read_perm(request.user, group, is_member, is_private)
allow_write = has_write_perm(request.user, group, is_member)
if not allow_read:
return HttpResponseForbidden()
articles = articles.order_by('title')
template_params = {'articles': articles, 'allow_write': allow_write}
if group_slug is not None:
template_params['group'] = group
new_article = ArticleClass(title='NewArticle')
new_article = ArticleClass(title='NewArticle', content_type=get_ct(group),
    object_id=group.id)
template_params['new_article'] = new_article
if extra_context is not None:
template_params.update(extra_context)
return render_to_response('/'.join([template_dir, template_name]),
    template_params, context_instance=RequestContext(request))
