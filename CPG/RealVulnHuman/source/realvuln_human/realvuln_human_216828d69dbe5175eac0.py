# Do not show tracing error the first time a user hits the GraphiQL endpoint.
        if 'GraphiQL Access Rejected' not in message:
            if 'extensions' not in formatted_error:
                formatted_error['extensions'] = {}

            # Get some stack traces and caller file information
            frame = inspect.currentframe()
            caller_frame = inspect.stack()[0]
            caller_filename_full = caller_frame.filename

            formatted_error['extensions']['exception'] = {}
            formatted_error['extensions']['exception']['stack'] = traceback.format_stack(frame)
            formatted_error['extensions']['exception']['debug'] = traceback.format_exc()
            formatted_error['extensions']['exception']['path'] = caller_filename_full

    return formatted_error

def format_execution_result(execution_result, format_error,):
    status_code = 200
    if execution_result:
        target_result = None

        def override_target_result(value):
            nonlocal target_result
