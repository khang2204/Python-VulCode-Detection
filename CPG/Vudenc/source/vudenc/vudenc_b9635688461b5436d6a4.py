def kill_and_wait(proc, grace_period, reason):...
logging.warning('SIGTERM finally due to %s', reason)
proc.terminate()
proc.wait(grace_period)
logging.warning('SIGKILL finally due to %s', reason)
exit_code = proc.wait()
proc.kill()
logging.info('Waiting for proces exit in finally - done')
return exit_code
