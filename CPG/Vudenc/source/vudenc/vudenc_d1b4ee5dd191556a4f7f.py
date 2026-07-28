def article_diff(request):...
"""docstring"""
current_article = get_object_or_404(Article, pk=int(request.POST['article']))
content = request.POST['body']
diffs = dmp.diff_main(current_article.content, content)
dmp.diff_cleanupSemantic(diffs)
return HttpResponse(dmp.diff_prettyHtml(diffs), content_type='text/html')
