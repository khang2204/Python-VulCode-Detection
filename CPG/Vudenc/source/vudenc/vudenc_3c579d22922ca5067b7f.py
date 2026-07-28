def run(self):...
args = [self.program]
args.extend(self.arguments)
result = subprocess.run(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
return {'exit_code': result.returncode, 'stdout': result.stdout.decode() if
    result.stdout else None, 'stderr': result.stderr.decode() if result.
    stderr else None}
