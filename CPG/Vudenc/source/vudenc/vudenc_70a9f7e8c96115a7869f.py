@login_required...
if request.method == 'POST':
revision = int(request.POST['revision'])
return HttpResponseNotAllowed(['POST'])
article_args = {'title': title}
group = None
if group_slug is not None:
group = get_object_or_404(group_qs, **{group_slug_field: group_slug})
allow_read = allow_write = True
article_args.update({'content_type': get_ct(group), 'object_id': group.id})
if not (allow_read or allow_write):
allow_read = has_read_perm(request.user, group, is_member, is_private)
return HttpResponseForbidden()
article = get_object_or_404(article_qs, **article_args)
allow_write = has_write_perm(request.user, group, is_member)
old_title = article.changeset_set.filter(revision=revision + 1).get().old_title
art = Article.objects.exclude(pk=article.pk).get(title=old_title)
if request.user.is_authenticated():
messages.error(request, 
    "Reverting not possible because an article with name '%s' already exists" %
    old_title)
article.revert_to(revision, get_real_ip(request), request.user)
article.revert_to(revision, get_real_ip(request))
return redirect(article)
return redirect(article)
