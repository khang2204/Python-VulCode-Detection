def main():...
"""docstring"""
defaults = {'TEST_STACK': str(AwsSmokeTestScenario.DEFAULT_TEST_ID),
    'TEST_APP': 'smoketest' + AwsSmokeTestScenario.DEFAULT_TEST_ID}
return st.ScenarioTestRunner.main(AwsSmokeTestScenario,
    default_binding_overrides=defaults, test_case_list=[AwsSmokeTest])
