def tpl_oneline(string):...
if string[0] == '%':
string = '\\' + string
return string
