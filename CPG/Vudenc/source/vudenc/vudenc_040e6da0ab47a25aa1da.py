def main():...
"""docstring"""
defaults = {'TEST_APP': 'awskatotest' + AwsKatoTestScenario.DEFAULT_TEST_ID}
return st.ScenarioTestRunner.main(AwsKatoTestScenario,
    default_binding_overrides=defaults, test_case_list=[AwsKatoIntegrationTest]
    )
