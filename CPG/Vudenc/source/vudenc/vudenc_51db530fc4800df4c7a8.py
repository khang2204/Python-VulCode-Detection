def set_executing(on: bool):...
"""docstring"""
my_thread = threading.current_thread()
if isinstance(my_thread, threads.CauldronThread):
my_thread.is_executing = on
