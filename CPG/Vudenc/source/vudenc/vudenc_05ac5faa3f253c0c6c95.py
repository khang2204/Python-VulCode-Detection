def get_frontend_routes():...
return [webapp2.Route('/restricted/ereporter2/errors',
    RestrictedEreporter2ErrorsList), webapp2.Route(
    '/restricted/ereporter2/errors/<error_id:\\d+>',
    RestrictedEreporter2Error), webapp2.Route(
    '/restricted/ereporter2/report', RestrictedEreporter2Report), webapp2.
    Route('/restricted/ereporter2/request/<request_id:[0-9a-fA-F]+>',
    RestrictedEreporter2Request), webapp2.Route(
    '/restricted/ereporter2/silence', RestrictedEreporter2Silence), webapp2
    .Route('/ereporter2/api/v1/on_error', OnErrorHandler)]
