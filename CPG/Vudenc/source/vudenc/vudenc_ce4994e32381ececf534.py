def query(self, cmd):...
"""docstring"""
data = {'code': 'from google.appengine.ext import db\n' + cmd, 'xsrf_token':
    self.xsrf_token}
result = self.post('_ah/admin/interactive/execute', data)
match = re.search(re.escape('<pre id="output">') + '(.*?)' + re.escape(
    """</pre>
</body>
</html>
"""), result, re.DOTALL)
return match.group(1)
