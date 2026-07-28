def exec_test():...
step.test_locals = dict()
step.test_locals.update(module.__dict__)
exec(code, step.test_locals)
