def test_bot_call_later_cancel(self):...
obj = bot.Bot(None, {}, 'https://localhost:1/', '1234-1a2b3c4-tainted-joe',
    'base_dir', None)
ev = threading.Event()
obj.call_later(0.1, ev.set)
obj.cancel_all_timers()
self.assertFalse(ev.wait(0.3))
