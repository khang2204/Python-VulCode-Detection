def history(request, group_slug=None, group_slug_field=None, group_qs=None,...
if request.method == 'GET':
if group_slug is not None:
return HttpResponseNotAllowed(['GET'])
group = get_object_or_404(group_qs, **{group_slug_field: group_slug})
allow_read = allow_write = True
changes_qs = changes_qs.filter(article__content_type=get_ct(group),
    article__object_id=group.id)
if not allow_read:
allow_read = has_read_perm(request.user, group, is_member, is_private)
return HttpResponseForbidden()
template_params = {'changes': changes_qs.order_by('-modified'),
    'allow_write': allow_write}
allow_write = has_write_perm(request.user, group, is_member)
if group_slug is not None:
template_params['group'] = group_slug
if extra_context is not None:
template_params.update(extra_context)
return render_to_response('/'.join([template_dir, template_name]),
    template_params, context_instance=RequestContext(request))
