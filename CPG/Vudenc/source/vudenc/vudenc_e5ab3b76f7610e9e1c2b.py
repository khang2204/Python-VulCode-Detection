def reset_dut(self, attempts=5):...
super().reset_dut(['- TARGET: processing user reset request',
    '- BDI asserts HRESET', '- Reset JTAG controller passed',
    '- JTAG exists check passed', '- BDI removes HRESET',
    '- TARGET: resetting target passed',
    '- TARGET: processing target startup \\.\\.\\.\\.',
    '- TARGET: processing target startup passed'], attempts)
