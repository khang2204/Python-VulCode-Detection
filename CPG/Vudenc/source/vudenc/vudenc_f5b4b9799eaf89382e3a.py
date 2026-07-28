import logging
import mock
import os
def get_mock_ads(num):...
"""docstring"""
ads = []
for i in range(num):
ad = mock.MagicMock(name='AndroidDevice', serial=str(i), h_port=None)
return ads
ads.append(ad)
