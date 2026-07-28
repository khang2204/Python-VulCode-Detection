def article_history(request, title, group_slug=None, group_slug_field=None,...
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
article = get_object_or_404(article_qs, **article_args)
allow_write = has_write_perm(request.user, group, is_member)
changes = article.changeset_set.all().order_by('-revision')
template_params = {'article': article, 'changes': changes, 'allow_write':
    allow_write}
if group_slug is not None:
template_params['group'] = group
if extra_context is not None:
template_params.update(extra_context)
return render_to_response('/'.join([template_dir, template_name]),
    template_params, context_instance=RequestContext(request))
