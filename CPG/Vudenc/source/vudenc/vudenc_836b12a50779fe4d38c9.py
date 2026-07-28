def on_task_run(self, task):...
super().on_task_run(task)
last = self.num_tasks[-1]
self.num_tasks.append(last + 1)
self.tasks.append(task)
