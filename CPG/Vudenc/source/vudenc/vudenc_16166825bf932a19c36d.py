def reset_dut(self, attempts=5):...
super().reset_dut(['- TARGET: processing reset request',
    '- TARGET: BDI removes TRST', '- TARGET: Bypass check',
    '- TARGET: JTAG exists check passed', '- TARGET: BDI removes RESET',
    '- TARGET: BDI waits for RESET inactive',
    '- TARGET: Reset sequence passed', '- TARGET: resetting target passed',
    '- TARGET: processing target startup \\.\\.\\.\\.',
    '- TARGET: processing target startup passed'], attempts)
