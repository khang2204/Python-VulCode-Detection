def run(self):...
"""docstring"""
self.input_channel.basic_consume(self.handle_message, queue=self.
    INPUT_QUEUE_NAME, no_ack=True)
self.input_channel.start_consuming()
log.info(' Exiting')
self.exit()
