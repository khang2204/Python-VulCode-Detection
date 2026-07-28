def render_executable(path, config):...
p = subprocess.Popen([path], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
stdout, stderr = p.communicate(json.dumps(config))
p.wait()
if p.returncode != 0:
return stdout
