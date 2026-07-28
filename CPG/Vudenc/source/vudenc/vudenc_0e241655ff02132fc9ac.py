def add_tracker(self, tracker_url):...
sanitized_url = get_uniformed_tracker_url(tracker_url)
if sanitized_url:
tracker = db.TrackerState.get(url=sanitized_url) or db.TrackerState(url=
    sanitized_url)
self.health.trackers.add(tracker)
