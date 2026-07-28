def run_file(runfile, func_to_get='main'):...
import_path, name = _guess_import_path_and_name(runfile)
if import_path not in sys.path:
sys.path.insert(0, import_path)
sys.modules['__tng_runfile__'] = module = imp.load_source(name, runfile)
if hasattr(module, func_to_get):
return getattr(module, func_to_get)
logging.getLogger('tng').warn('No {} function found in {}'.format(
    func_to_get, runfile))
