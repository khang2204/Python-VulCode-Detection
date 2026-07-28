def test_bot(self):...
obj = bot.Bot(None, {'dimensions': {'foo': 'bar'}}, 'https://localhost:1/',
    '1234-1a2b3c4-tainted-joe', 'base_dir', None)
self.assertEqual({'foo': 'bar'}, obj.dimensions)
self.assertEqual(os.path.join(os.path.dirname(THIS_FILE),
    'swarming_bot.zip'), obj.swarming_bot_zip)
self.assertEqual('1234-1a2b3c4-tainted-joe', obj.server_version)
self.assertEqual('base_dir', obj.base_dir)
