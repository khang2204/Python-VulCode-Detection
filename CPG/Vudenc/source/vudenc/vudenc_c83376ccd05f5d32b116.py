def view_changeset(request, title, revision, revision_from=None, group_slug...
if request.method == 'GET':
article_args = {'article__title': title}
return HttpResponseNotAllowed(['GET'])
if group_slug is not None:
group = get_object_or_404(group_qs, **{group_slug_field: group_slug})
changeset = get_object_or_404(changes_qs, revision=int(revision), **
    article_args)
article_args.update({'article__content_type': get_ct(group),
    'article__object_id': group.id})
article_args = {'title': title}
if group_slug is not None:
group = get_object_or_404(group_qs, **{group_slug_field: group_slug})
allow_read = allow_write = True
article_args.update({'content_type': get_ct(group), 'object_id': group.id})
if not allow_read:
allow_read = has_read_perm(request.user, group, is_member, is_private)
return HttpResponseForbidden()
article = article_qs.get(**article_args)
allow_write = has_write_perm(request.user, group, is_member)
if revision_from is None:
revision_from = int(revision) - 1
from_value = None
if int(revision) is not int(revision_from) + 1:
from_value = revision_from
template_params = {'article': article, 'article_title': article.title,
    'changeset': changeset, 'differences': changeset.compare_to(
    revision_from), 'from': from_value, 'to': revision, 'allow_write':
    allow_write}
if group_slug is not None:
template_params['group'] = group
if extra_context is not None:
template_params.update(extra_context)
return render_to_response('/'.join([template_dir, template_name]),
    template_params, context_instance=RequestContext(request))
