def test_cookie(self):...
token = (
    'a7MPUEQQLAEEQEAQDGJOXKAMFM467EUW6HCETFI4VP5JCU3CDVJDQZSHMXAOSCU25WPZA66NY5ZVAA4RPCVMHBQBJSVGYQPPLZNIBTP3Y'
    )
sessid = 'fb1f42420b0109020203325d750185673df252de388932a3957f522a6c43aa47'
self.redis_instance.conn.set(sessid, json.dumps({'v1': {'id': '0'}}))
eppn = self.test_user_data['eduPersonPrincipalName']
self.assertRaises(NotFound, c.get, '/')
