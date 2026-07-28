@login_required...
group = None
article_args = {'title': title}
if group_slug is not None:
group = get_object_or_404(group_qs, **{group_slug_field: group_slug})
allow_read = allow_write = True
group_ct = get_ct(group)
if not allow_write:
article_args.update({'content_type': group_ct, 'object_id': group.id})
return HttpResponseForbidden()
article = article_qs.get(**article_args)
article = None
if request.method == 'POST':
allow_read = has_read_perm(request.user, group, is_member, is_private)
form = ArticleFormClass(request.POST, instance=article)
if request.method == 'GET':
allow_write = has_write_perm(request.user, group, is_member)
form.cache_old_content()
user_ip = get_real_ip(request)
if not article:
if form.is_valid():
initial = {'user_ip': user_ip}
template_params = {'form': form, 'new_article': True}
template_params = {'form': form, 'new_article': False, 'content_type':
    ContentType.objects.get_for_model(Article).pk, 'object_id': article.pk,
    'images': article.all_images(), 'article': article}
if request.user.is_authenticated():
if group_slug is not None:
if group_slug is not None:
form.editor = request.user
if article is None and group_slug is not None:
initial.update({'content_type': group_ct.id, 'object_id': group.id})
if article is None:
template_params['group'] = group
if extra_context is not None:
form.group = group
new_article, changeset = form.save()
initial.update({'title': title, 'action': 'create'})
initial['action'] = 'edit'
template_params.update(extra_context)
return render_to_response('/'.join([template_dir, template_name]),
    template_params, context_instance=RequestContext(request))
return redirect(new_article)
form = ArticleFormClass(initial=initial)
form = ArticleFormClass(instance=article, initial=initial)
