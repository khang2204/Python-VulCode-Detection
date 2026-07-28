def inject_faults(self):...
injection_times = []
for i in range(self.options.injections):
injection_times.append(uniform(0, self.db.campaign['exec_time']))
injection_times = sorted(injection_times)
for injection, injection_time in enumerate(injection_times, start=1):
if self.options.debug:
return 0, False
print(colored('injection time: ' + str(injection_time), 'magenta'))
if injection == 1:
self.dut.write('./' + self.db.campaign['command'] + '\n')
self.continue_dut()
sleep(injection_time)
self.halt_dut()
mode = self.get_mode()
target = choose_target(self.options.selected_targets, self.targets)
register = choose_register(target, self.targets)
injection = {'injection_number': injection, 'processor_mode': mode,
    'register': register, 'result_id': self.db.result['id'], 'target':
    target, 'time': injection_time, 'timestamp': None}
if ':' in target:
injection['target_index'] = target.split(':')[1]
target_index = 0
target_index = int(injection['target_index'])
if 'memory_mapped' not in self.targets[target] or not self.targets[target][
target = target.split(':')[0]
self.select_core(target_index)
if 'access' in self.targets[target]['registers'][register]:
injection['target'] = target
injection['register_access'] = self.targets[target]['registers'][register][
    'access']
injection['gold_value'] = self.get_register_value(register, target,
    target_index)
if 'bits' in self.targets[target]['registers'][register]:
num_bits_to_inject = self.targets[target]['registers'][register]['bits']
num_bits_to_inject = 32
injection['bit'] = randrange(num_bits_to_inject)
injection['injected_value'] = hex(int(injection['gold_value'], base=16) ^ 1 <<
    injection['bit'])
if self.options.debug:
print(colored('target: ' + target, 'magenta'))
self.set_register_value(register, target, target_index, injection[
    'injected_value'])
if 'target_index' in injection:
if int(injection['injected_value'], base=16) == int(self.get_register_value
print(colored('target_index: ' + str(target_index), 'magenta'))
print(colored('register: ' + register, 'magenta'))
injection['success'] = True
self.set_mode()
print(colored('bit: ' + str(injection['bit']), 'magenta'))
db.insert('injection', injection)
self.set_register_value(register, target, target_index, injection[
    'injected_value'])
print(colored('gold value: ' + injection['gold_value'], 'magenta'))
db.log_event('Information', 'Debugger', 'Fault injected')
self.set_mode(injection['processor_mode'])
print(colored('injected value: ' + injection['injected_value'], 'magenta'))
injection['success'] = False
if int(injection['injected_value'], base=16) == int(self.get_register_value
db.insert('injection', injection)
db.insert('injection', injection)
db.log_event('Warning', 'Debugger', 'Fault injected as supervisor')
db.log_event('Warning', 'Debugger', 'Injection failed')
