def test_when_there_is_a_dynamic_link_wraps_public_domain_url(self):...
RedirectExperienceTestCase.ScenarioMaker().given_an_experience_on_db(title=
    'a', description='d', share_id='AsdE43E4', pic='url'
    ).given_a_public_domain('http://pachatary.com').given_a_dynamic_link(
    'http://dynamic.link/link={}&other=param').when_call_experience_redirect(
    'AsdE43E4').then_response_should_be_a_redirect_to(
    'http://dynamic.link/link=http://pachatary.com/e/AsdE43E4&other=param&st=a&sd=d&si=%2Fmedia%2Furl.small'
    )
