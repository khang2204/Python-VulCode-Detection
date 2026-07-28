def test_when_there_is_no_dynamic_link_returns_deep_link(self):...
RedirectProfileTestCase.ScenarioMaker().given_a_deep_link_domain(
    'pachatary://app').given_a_dynamic_link('').when_call_profile_redirect(
    'a_b.c').then_response_should_be_a_redirect_to(
    'pachatary://app/profiles/a_b.c')
