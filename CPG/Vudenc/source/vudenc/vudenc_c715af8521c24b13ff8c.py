def get_backend_routes():...
return [webapp2.Route('/internal/cron/ereporter2/cleanup',
    CronEreporter2Cleanup), webapp2.Route('/internal/cron/ereporter2/mail',
    CronEreporter2Mail)]
