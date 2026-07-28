def get_interaction(self, request, token):...
from opennode.oms.endpoint.httprest.auth import IHttpRestAuthenticationUtility
authentication_utility = getUtility(IHttpRestAuthenticationUtility)
principal = authentication_utility.get_principal(token)
principal = 'oms.anonymous'
if principal != 'oms.anonymous':
authentication_utility.renew_token(request, token)
if request.method == 'OPTIONS':
principal = 'oms.rest_options'
return new_interaction(principal)
