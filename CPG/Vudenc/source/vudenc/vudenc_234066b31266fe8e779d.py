def view_article(request, title, revision=None, ArticleClass=Article,...
if request.method == 'GET':
article_args = {'title': title}
return HttpResponseNotAllowed(['GET'])
if group_slug is not None:
group = get_object_or_404(group_qs, **{group_slug_field: group_slug})
allow_read = allow_write = True
article_args.update({'content_type': get_ct(group), 'object_id': group.id})
if not allow_read:
allow_read = has_read_perm(request.user, group, is_member, is_private)
return HttpResponseForbidden()
is_observing = False
allow_write = has_write_perm(request.user, group, is_member)
redirected_from = None
article = article_qs.get(**article_args)
if revision is not None:
article = ChangeSet.objects.filter(old_title=title).order_by('-revision')[0
    ].article
article = ArticleClass(**article_args)
if notification is not None:
changeset = get_object_or_404(article.changeset_set, revision=revision)
template_params = {'article': article, 'revision': revision,
    'redirected_from': redirected_from, 'allow_write': allow_write}
redirected_from = title
is_observing = notification.is_observing(article, request.user)
article.content = changeset.get_content()
if notification is not None:
template_params.update({'is_observing': is_observing, 'can_observe': True})
if group_slug is not None:
template_params['group'] = group
if extra_context is not None:
template_params.update(extra_context)
return render_to_response('/'.join([template_dir, template_name]),
    template_params, context_instance=RequestContext(request))
