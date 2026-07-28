def setup_logging(self):...
self.log_area = QTextEdit()
self.log_area.setReadOnly(True)
self.log_queue = queue.Queue()
self.log_stream = LoggingStream(self.log_queue)
self.log_thread = LoggingThread(self.log_queue, parent=self)
self.log_thread.message_received.connect(self.log)
self.log_thread.start()
