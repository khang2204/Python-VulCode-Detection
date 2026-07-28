def setUp(self):...
super().setUp()
self.runner = executors.Runner(policies.AsynchronousExecutionPolicy())
self.runner.policy.keep_stage_files = True
self.monitor = TaskEventMonitor()
self.runner.policy.task_listeners.append(self.monitor)
