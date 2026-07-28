def BuildRequestData(start_column=None, query=None, include_buffer_data=True):...
line, column = vimsupport.CurrentLineAndColumn()
filepath = vimsupport.GetCurrentBufferFilepath()
request_data = {'filetypes': vimsupport.CurrentFiletypes(), 'line_num':
    line, 'column_num': column, 'start_column': start_column, 'line_value':
    vim.current.line, 'filepath': filepath}
if include_buffer_data:
request_data['file_data'] = vimsupport.GetUnsavedAndCurrentBufferData()
if query:
request_data['query'] = query
return request_data
