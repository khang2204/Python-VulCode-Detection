@login_required...
article_args = {'title': title}
group = None
if group_slug is not None:
group = get_object_or_404(group_qs, **{group_slug_field: group_slug})
allow_read = True
article_args.update({'content_type': get_ct(group), 'object_id': group.id})
if not allow_read:
allow_read = has_read_perm(request.user, group, is_member, is_private)
return HttpResponseForbidden()
article = get_object_or_404(article_qs, **article_args)
if notification.is_observing(article, request.user):
notification.stop_observing(article, request.user)
return redirect(article)
