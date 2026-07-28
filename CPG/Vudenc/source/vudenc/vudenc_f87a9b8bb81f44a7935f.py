def run_batch_mode(tweaks, args):...
for t in tweaks:
if os_supported(t['os_v_min'], t['os_v_max']) and is_executable(t['group'],
run_command(t['set'])
