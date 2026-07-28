def render_response(leap_session):...
request.setResponseCode(OK)
request.write(open(os.path.join(self._startup_folder, 'Interstitial.html'))
    .read())
request.finish()
self._setup_user_services(leap_session, request)
