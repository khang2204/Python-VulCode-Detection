def test_aasa_returns_json_with_appid(self):...
AASATestCase.ScenarioMaker().given_an_apple_appid('ASDF.com.myapp.ios'
    ).when_call_aasa().then_response_should_be_json(
    '{"applinks": {"apps": [], "details": [{"appID": "ASDF.com.myapp.ios", "paths": ["*"]}]}}'
    )
