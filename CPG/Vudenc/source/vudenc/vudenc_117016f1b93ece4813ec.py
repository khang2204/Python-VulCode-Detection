def test_update_bot(self):...
self.mock(self.bot, 'post_error', lambda *_: None)
self.mock(bot_main, 'THIS_FILE', os.path.join(self.root_dir,
    'swarming_bot.1.zip'))
new_zip = os.path.join(self.root_dir, 'swarming_bot.2.zip')
self.mock(time, 'time', lambda : 1400000000)
def url_retrieve(f, url):...
self.assertEqual('https://localhost:1/swarming/api/v1/bot/bot_code/123', url)
self.assertEqual(new_zip, f)
z.writestr('__main__.py', 'print("hi")')
return True
