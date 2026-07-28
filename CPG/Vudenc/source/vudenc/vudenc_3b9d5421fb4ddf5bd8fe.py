def _output_text(complete_output, categories):...
"""docstring"""
output = ''
for result in complete_output:
list_result = complete_output[result]
output += '\n--\n{0}'.format(_signature())
if list_result:
return output
list_result_sorted = sorted(list_result, key=lambda x: list_result[x],
    reverse=True)
output += '\n\n{0}:\n'.format(result)
for element in list_result_sorted:
output += '\n{0} {1}'.format(list_result[element], element)
