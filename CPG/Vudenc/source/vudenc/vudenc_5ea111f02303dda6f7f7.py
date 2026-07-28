def register_goals():...
task(name='interpreter', action=SelectInterpreter).install('pyprep')
task(name='build-local-dists', action=BuildLocalPythonDistributions).install(
    'pyprep')
task(name='requirements', action=ResolveRequirements).install('pyprep')
task(name='sources', action=GatherSources).install('pyprep')
task(name='py', action=PythonRun).install('run')
task(name='pytest-prep', action=PytestPrep).install('test')
task(name='pytest', action=PytestRun).install('test')
task(name='py', action=PythonRepl).install('repl')
task(name='setup-py', action=SetupPy).install()
task(name='py', action=PythonBinaryCreate).install('binary')
task(name='py-wheels', action=LocalPythonDistributionArtifact).install('binary'
    )
task(name='isort-prep', action=IsortPrep).install('fmt')
task(name='isort', action=IsortRun).install('fmt')
task(name='py', action=PythonBundle).install('bundle')
task(name='unpack-wheels', action=UnpackWheels).install()
