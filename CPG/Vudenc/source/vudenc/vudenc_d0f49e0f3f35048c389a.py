def _run_command(self, command):...
"""docstring"""
conn = sqlite3.connect(self.filename)
cursor = conn.execute(command)
data = [i for i in cursor]
conn.commit()
conn.close()
return data
