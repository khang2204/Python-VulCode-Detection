def DownloadFile(local_file, url):...
"""docstring"""
local_file = os.path.abspath(local_file)
url_data = UrlOpen(url, method='GET')
if url_data is None:
return False
f.write(url_data)
logging.error("""Failed to write to %s
%s""", local_file, e)
return True
return False
