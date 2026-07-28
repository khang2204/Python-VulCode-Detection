def login(self, username, password):...
"""docstring"""
login_url = 'https://www.kijiji.ca/t-login.html'
resp = self.session.get(login_url)
payload = {'emailOrNickname': username, 'password': password, 'rememberMe':
    'true', '_rememberMe': 'on', 'ca.kijiji.xsrf.token': get_token(resp.
    text, 'ca.kijiji.xsrf.token'), 'targetUrl':
    'L3QtbG9naW4uaHRtbD90YXJnZXRVcmw9TDNRdGJHOW5hVzR1YUhSdGJEOTBZWEpuWlhSVmNtdzlUREpuZEZwWFVuUmlNalV3WWpJMGRGbFlTbXhaVXpoNFRucEJkMDFxUVhsWWJVMTZZbFZLU1dGVmJHdGtiVTVzVlcxa1VWSkZPV0ZVUmtWNlUyMWpPVkJSTFMxZVRITTBVMk5wVW5wbVRHRlFRVUZwTDNKSGNtVk9kejA5XnpvMnFzNmc2NWZlOWF1T1BKMmRybEE9PQ--'
    }
resp = self.session.post(login_url, data=payload)
if not self.is_logged_in():
