def start_clear_holders_deps():...
"""docstring"""
mdadm.mdadm_assemble(scan=True, ignore_errors=True)
util.subp(['modprobe', 'bcache'], rcs=[0, 1])
