def respond_text(text):...
response = HttpResponse(text)
response['Access-Control-Allow-Origin'] = '*'
return response
