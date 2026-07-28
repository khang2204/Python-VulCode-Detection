def fetch_file(url):...
"""docstring"""
filename = os.path.basename(url)
if os.path.exists(filename):
return
r = requests.get(url, stream=True)
r.raise_for_status()
for chunk in r.iter_content(4096):
fd.write(chunk)
