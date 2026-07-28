def get_backend_routes():...
prpc_server = prpc.Server()
prpc_server.add_interceptor(auth.prpc_interceptor)
prpc_server.add_service(api.BuildsApi())
return [webapp2.Route('/internal/cron/buildbucket/expire_build_leases',
    expiration.CronExpireBuildLeases), webapp2.Route(
    '/internal/cron/buildbucket/expire_builds', expiration.CronExpireBuilds
    ), webapp2.Route('/internal/cron/buildbucket/delete_builds', expiration
    .CronDeleteBuilds), webapp2.Route(
    '/internal/cron/buildbucket/update_buckets', CronUpdateBuckets),
    webapp2.Route('/internal/cron/buildbucket/bq-export-prod', bq.
    CronExportBuildsProd), webapp2.Route(
    '/internal/cron/buildbucket/bq-export-experimental', bq.
    CronExportBuildsExperimental), webapp2.Route(
    '/internal/cron/buildbucket/unregister-builders', UnregisterBuilders),
    webapp2.Route('/internal/task/buildbucket/notify/<build_id:\\d+>',
    notifications.TaskPublishNotification), webapp2.Route(
    '/internal/task/buildbucket/cancel_swarming_task/<host>/<task_id>',
    TaskCancelSwarmingTask)] + bulkproc.get_routes() + prpc_server.get_routes()
