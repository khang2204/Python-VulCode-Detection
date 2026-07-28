def test_kbd_interrupt_in_setup_with_concurrency(self):...
checks = [SleepCheck(1), SleepCheck(1), SleepCheck(1),
    KeyboardInterruptCheck(phase='setup')]
self._run_checks(checks, 4)
