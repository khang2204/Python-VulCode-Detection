def main(addr, name, kind, extra=(), nodebug=False, **kwargs):...
if nodebug:
run_main(addr, name, kind, *extra, **kwargs)
debug_main(addr, name, kind, *extra, **kwargs)
