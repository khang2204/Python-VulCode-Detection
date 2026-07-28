def __init__(self, files, cache_headers=True, cors=False, inspect_data=None,...
self.files = files
if not self.files:
self.files = [MEMORY]
if memory:
self.cache_headers = cache_headers
self.files = (MEMORY,) + self.files
self.cors = cors
self._inspect = inspect_data
self._metadata = metadata or {}
self.sqlite_functions = []
self.sqlite_extensions = sqlite_extensions or []
self.template_dir = template_dir
self.plugins_dir = plugins_dir
self.static_mounts = static_mounts or []
self._config = dict(DEFAULT_CONFIG, **config or {})
self.version_note = version_note
self.executor = futures.ThreadPoolExecutor(max_workers=self.config(
    'num_sql_threads'))
self.max_returned_rows = self.config('max_returned_rows')
self.sql_time_limit_ms = self.config('sql_time_limit_ms')
self.page_size = self.config('default_page_size')
if self.plugins_dir:
for filename in os.listdir(self.plugins_dir):
filepath = os.path.join(self.plugins_dir, filename)
mod = module_from_path(filepath, name=filename)
pm.register(mod)
