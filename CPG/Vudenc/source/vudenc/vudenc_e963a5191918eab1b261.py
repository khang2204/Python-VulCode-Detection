@pyqtSlot()...
self.status_monitor_queue.put(ExitFlag())
self.status_monitor.update_thread.wait()
self.log_queue.put(ExitFlag())
self.log_thread.wait()
