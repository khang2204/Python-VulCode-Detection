def check_auth(self, request):...
from opennode.oms.endpoint.httprest.auth import IHttpRestAuthenticationUtility
authentication_utility = getUtility(IHttpRestAuthenticationUtility)
credentials = authentication_utility.get_basic_auth_credentials(request)
if credentials:
blocking_yield(authentication_utility.authenticate(request, credentials,
    basic_auth=True))
return authentication_utility.get_token(request)
return authentication_utility.generate_token(credentials)
