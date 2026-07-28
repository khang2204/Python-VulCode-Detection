def create_test(self, name):...
test = rfm.RegressionTest()
test.name = name
test.valid_systems = ['*']
test.valid_prog_environs = ['*']
test.executable = 'echo'
test.executable_opts = [name]
return test
