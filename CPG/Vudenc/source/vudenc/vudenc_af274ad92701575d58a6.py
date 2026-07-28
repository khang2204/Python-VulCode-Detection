def render_error(error):...
log.info('Login Error for %s' % request.args['username'][0])
log.info('%s' % error)
request.setResponseCode(UNAUTHORIZED)
return self._render_template(request, 'Invalid credentials')
