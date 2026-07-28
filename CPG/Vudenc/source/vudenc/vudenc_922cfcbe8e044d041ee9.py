def select_row_from_mysql_command(command_str):...
"""docstring"""
""" OUPUT: a list of elements in the selected row """
sql = text(str(command_str))
return s.execute(sql).fetchall()
