def main():...
"""docstring"""
defaults = {'TEST_STACK': str(GoogleSmokeTestScenario.DEFAULT_TEST_ID),
    'TEST_APP': 'gcpsmoketest' + GoogleSmokeTestScenario.DEFAULT_TEST_ID}
return st.ScenarioTestRunner.main(GoogleSmokeTestScenario,
    default_binding_overrides=defaults, test_case_list=[GoogleSmokeTest])
