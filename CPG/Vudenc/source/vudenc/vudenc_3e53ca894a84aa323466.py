def rules():...
return [run_python_test, UnionRule(TestTarget, PythonTestsAdaptor),
    optionable_rule(PyTest), optionable_rule(PythonSetup), optionable_rule(
    SourceRootConfig)]
