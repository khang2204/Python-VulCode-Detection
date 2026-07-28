def test_when_there_is_a_dynamic_link_wraps_public_domain_url(self):...
RedirectRootTestCase.ScenarioMaker().given_a_public_domain(
    'http://pachatary.com').given_a_dynamic_link(
    'http://dynamic.link/link={}&other=param').when_call_root_redirect(
    ).then_response_should_be_a_redirect_to(
    'http://dynamic.link/link=http://pachatary.com/&other=param')
