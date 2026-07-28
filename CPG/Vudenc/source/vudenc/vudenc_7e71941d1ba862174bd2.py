def handle_evaluate(self, reqid, interface, method, data):...
domain, page = data
self.p.log.info('Recvd page %s, working on', reqid)
res = self.ev.solve_capage(domain, page)
self.p.log.info('Done, sending answer: %s', res)
self.p.send_success_rep(reqid, [v.encode('utf-8') for v in res])
