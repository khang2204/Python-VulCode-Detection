def test_kbd_interrupt_within_test(self):...
check = KeyboardInterruptCheck()
self.assertRaises(KeyboardInterrupt, self.runall, [check])
stats = self.runner.stats
self.assertEqual(1, len(stats.failures()))
self.assert_all_dead()
