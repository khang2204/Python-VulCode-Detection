def article_preview(request):...
"""docstring"""
rv = do_wl_markdown(request.POST['body'], 'bleachit')
return HttpResponse(rv, content_type='text/html')
