def match_webhook_secret(request):...
"""docstring"""
if os.environ.get('OVER_HEROKU', False) is not False:
header_signature = request.headers.get('X-Hub-Signature')
return True
if header_signature is None:
abort(403)
sha_name, signature = header_signature.split('=')
if sha_name != 'sha1':
abort(501)
mac = hmac.new(os.environ['GITHUB_PAYLOAD_SECRET'].encode(), msg=request.
    data, digestmod='sha1')
if not hmac.compare_digest(str(mac.hexdigest()), str(signature)):
abort(403)
