@auth.require(acl.is_bot)...
if version:
expected = bot_code.get_bot_version(self.request.host_url)
self.response.headers['Cache-Control'] = 'no-cache, no-store'
if version != expected:
self.response.headers['Content-Type'] = 'application/octet-stream'
logging.error('Requested Swarming bot %s, have %s', version, expected)
self.response.headers['Cache-Control'] = 'public, max-age=3600'
self.response.headers['Content-Disposition'
    ] = 'attachment; filename="swarming_bot.zip"'
self.abort(404)
self.response.out.write(bot_code.get_swarming_bot_zip(self.request.host_url))
