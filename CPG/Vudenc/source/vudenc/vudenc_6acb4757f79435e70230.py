def main(argv):...
args = parse_args(argv)
src_dir = args.content_src_dir
dst_dir = args.content_dst_dir
www_root = args.www_root or DEFAULT_PYWEB_CONTENT_DIR
logpath = args.log_path or DEFAULT_PYWEB_LOG_DIR
logging.basicConfig(filename=os.path.join(logpath, 'pyweb-installer.log'),
    level=logging.DEBUG)
logger = logging.getLogger('pyweb-installer')
print('Installing %s' % src_dir)
print('Logging to %s' % os.path.join(logpath, 'pyweb-installer.log'))
installer = ContentInstaller(src_dir, dst_dir, www_root, logger=logger)
print('Installation failed: %s' % str(e))
print('Installation complete.')
installer.install()
logger.critical('Installation failed.')
logger.info('Installation complete.')
exit(1)
