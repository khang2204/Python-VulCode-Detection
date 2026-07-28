def open_events_socket(self, _):...
agent = Agent(reactor, pool=self.connection_pool)
return agent.request('GET', 'http://localhost:%s/events' % self.session.
    config.get_http_api_port(), Headers({'User-Agent': ['Tribler ' +
    version_id]}), None).addCallback(self.on_event_socket_opened)
