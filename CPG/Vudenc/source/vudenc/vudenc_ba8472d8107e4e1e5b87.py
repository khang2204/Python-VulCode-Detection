def check_component(comp, session, logger):...
logger.debug('Running component check for %s' % comp['name'])
check_available = len(comp['cmd']) > 1 and 'check' in comp['cmd'][1]
window = find_window(session, comp['name'])
if window:
pid = get_window_pid(window)
logger.debug('%s window is not running. Running custom check' % comp['name'])
logger.debug('Found window pid: %s' % pid)
if check_available and run_component_check(comp):
procs = []
logger.debug('Component was not started by Hyperion, but the check succeeded')
logger.debug(
    'Window not running and no check command is available or it failed: returning false'
    )
for entry in pid:
return CheckState.STARTED_BY_HAND
return CheckState.STOPPED
procs.extend(Process(entry).children(recursive=True))
pids = [p.pid for p in procs]
logger.debug('Window is running %s child processes' % len(pids))
if len(pids) < 3:
logger.debug(
    'Main window process has finished. Running custom check if available')
if check_available and run_component_check(comp):
if check_available and run_component_check(comp):
logger.debug('Check succeeded')
if not check_available:
logger.debug('Process terminated but check was successful')
logger.debug('Check failed or no check available: returning false')
return CheckState.RUNNING
logger.debug(
    'No custom check specified and got sufficient pid amount: returning true')
logger.debug('Check failed: returning false')
return CheckState.STOPPED_BUT_SUCCESSFUL
return CheckState.STOPPED
return CheckState.RUNNING
return CheckState.STOPPED
