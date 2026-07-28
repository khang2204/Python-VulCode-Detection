def render_POST(self, request):...
if self.is_logged_in(request):
return util.redirectTo('/', request)
def render_response(leap_session):...
request.setResponseCode(OK)
request.write(open(os.path.join(self._startup_folder, 'Interstitial.html'))
    .read())
request.finish()
self._setup_user_services(leap_session, request)
def render_error(error):...
log.info('Login Error for %s' % request.args['username'][0])
log.info('%s' % error)
request.setResponseCode(UNAUTHORIZED)
return self._render_template(request, 'Invalid credentials')
