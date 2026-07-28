def run_component_check(comp):...
if call(comp['cmd'][1]['check'], shell=True) == 0:
return True
return False
