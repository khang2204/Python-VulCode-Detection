def generate_config():...
arg = docopt(__doc__, version='0.1.0')
start_time = datetime.now()
file_name = MonitoringConfigGenerator(arg['URL'], arg['--debug'], arg[
    '--targetdir'], arg['--skip-checks']).generate()
LOG.warn('Target url {0} unreachable. Could not get yaml config!'.format(
    arg['URL']))
stop_time = datetime.now()
sys.exit(exit_code)
exit_code = EXIT_CODE_CONFIG_WRITTEN if file_name else EXIT_CODE_NOT_WRITTEN
exit_code = EXIT_CODE_NOT_WRITTEN
LOG.info('finished in %s' % (stop_time - start_time))
LOG.error('Configuration contained undefined variables!')
exit_code = EXIT_CODE_ERROR
exit_code = e.code
LOG.error(e)
exit_code = EXIT_CODE_ERROR
