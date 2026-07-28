def execute_io_loop(timeout):...
get_executing_test().addCleanup(require_io_loop_executor().stop)
require_io_loop_executor().execute(timeout=timeout)
get_executing_test().error = traceback.format_exc()
