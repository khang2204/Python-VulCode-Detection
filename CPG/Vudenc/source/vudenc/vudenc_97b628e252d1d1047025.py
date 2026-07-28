def __str__(self):...
string = """DrSEUs Attributes:
	Debugger: """ + str(self.debugger
    ) + '\n\tDUT:\t' + str(self.debugger.dut).replace('\n\t', '\n\t\t')
if self.campaign_data['use_aux']:
string += '\n\tAUX:\t' + str(self.debugger.aux).replace('\n\t', '\n\t\t')
string += """
	Campaign Information:
		Campaign Number: """ + str(self.
    campaign_data['id']) + """
		DUT Command: \"""" + self.campaign_data[
    'command'] + '"'
if self.campaign_data['use_aux']:
string += """
		AUX Command: \"""" + self.campaign_data['aux_command'] + '"'
string += '\n\t\t' + ('Host ' if self.campaign_data['use_simics'] else ''
    ) + 'Execution Time: ' + str(self.campaign_data['exec_time']) + ' seconds'
if self.campaign_data['use_simics']:
string += """
		Execution Cycles: """ + '{:,}'.format(self.campaign_data[
    'num_cycles']) + """ cycles
		Simulated Time: """ + str(self.
    campaign_data['sim_time']) + ' seconds'
return string
