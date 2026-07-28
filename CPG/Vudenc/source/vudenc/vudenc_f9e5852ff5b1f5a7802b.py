def tracked_files():...
p = Popen(['git', 'ls-tree', '-r', '--name-only', 'HEAD'], stdout=PIPE, env=env
    )
out = p.communicate()[0]
if p.returncode != 0 or not out.strip():
return None
return [e.strip() for e in out.splitlines() if os.path.exists(e)]
