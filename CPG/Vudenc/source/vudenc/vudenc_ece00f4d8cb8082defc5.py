def main():...
defaults = {'TEST_STACK': GoogleServerGroupTestScenario.DEFAULT_TEST_ID,
    'TEST_APP': 'gcpsvrgrptst' + GoogleServerGroupTestScenario.DEFAULT_TEST_ID}
return st.ScenarioTestRunner.main(GoogleServerGroupTestScenario,
    default_binding_overrides=defaults, test_case_list=[GoogleServerGroupTest])
