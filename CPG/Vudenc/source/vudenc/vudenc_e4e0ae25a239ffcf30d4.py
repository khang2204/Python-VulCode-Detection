def get_instances(serials):...
ads = []
for serial in serials:
ad = mock.MagicMock(name='AndroidDevice', serial=serial, h_port=None)
return ads
ads.append(ad)
