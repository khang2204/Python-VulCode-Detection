def _handle_workflow(self, session, data, headers):...
wf_engine.start_engine(session=session, input=data, workflow_name=data['wf'])
wf_engine.current.headers = headers
self.current = wf_engine.current
wf_engine.run()
return wf_engine.current.output
