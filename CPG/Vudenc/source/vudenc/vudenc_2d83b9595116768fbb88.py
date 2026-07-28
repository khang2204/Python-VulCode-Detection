def test_when_there_is_a_dynamic_link_wraps_public_domain_url(self):...
RedirectProfileTestCase.ScenarioMaker().given_a_profile(username='a_b.c',
    bio='my info', pic='url').given_a_public_domain('http://pachatary.com'
    ).given_a_dynamic_link('http://dynamic.link/link={}&other=param'
    ).when_call_profile_redirect('a_b.c'
    ).then_response_should_be_a_redirect_to(
    'http://dynamic.link/link=http://pachatary.com/p/a_b.c&other=param&st=%40a_b.c&sd=my+info&si=%2Fmedia%2Furl.small'
    )
