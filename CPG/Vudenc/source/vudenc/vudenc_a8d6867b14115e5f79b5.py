@handled_function...
self.status_monitor_queue = queue.Queue(maxsize=1)
self.status_monitor = StatusMonitor(self.matisse, self.status_monitor_queue)
self.layout.addWidget(self.status_monitor)
