def live_processes(self):...
"""docstring"""
result = []
for process_type, process_infos in self.all_processes.items():
for process_info in process_infos:
return result
if process_info.process.poll() is None:
result.append((process_type, process_info.process))
