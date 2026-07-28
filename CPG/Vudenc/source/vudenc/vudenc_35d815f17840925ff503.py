def execute_process_synchronously(self, execute_process_request, name,...
"""docstring"""
result = self._scheduler.product_request(FallibleExecuteProcessResult, [
    execute_process_request])[0]
workunit.output('stdout').write(result.stdout)
workunit.output('stderr').write(result.stderr)
workunit.set_outcome(WorkUnit.FAILURE if result.exit_code else WorkUnit.SUCCESS
    )
return result
