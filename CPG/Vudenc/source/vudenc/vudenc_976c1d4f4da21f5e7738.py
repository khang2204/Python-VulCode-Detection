def test_bot_call_later(self):...
obj = bot.Bot(None, {}, 'https://localhost:1/', '1234-1a2b3c4-tainted-joe',
    'base_dir', None)
ev = threading.Event()
obj.call_later(0.001, ev.set)
self.assertTrue(ev.wait(1))
