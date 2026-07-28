def test_kbd_interrupt_in_wait_with_concurrency(self):...
checks = [KeyboardInterruptCheck(), SleepCheck(10), SleepCheck(10),
    SleepCheck(10)]
self._run_checks(checks, 4)
