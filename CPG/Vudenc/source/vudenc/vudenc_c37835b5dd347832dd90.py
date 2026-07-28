def term_handler(interface, method, data):...
self.log.info('Termination signal %s recieved', repr((interface, method, data))
    )
self.term()
