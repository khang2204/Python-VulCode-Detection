def monkeypatch_pyramid_csrf_check():...
from pyramid import session
def check_csrf_token(request, token='csrf_token', header=HEADER_NAME,...
supplied_token = request.params.get(token, request.headers.get(header))
if supplied_token != request.session.get_csrf_token():
if raises:
return True
return False
