def GetTagFiles():...
tag_files = vim.eval('tagfiles()')
current_working_directory = os.getcwd()
return [os.path.join(current_working_directory, x) for x in tag_files]
