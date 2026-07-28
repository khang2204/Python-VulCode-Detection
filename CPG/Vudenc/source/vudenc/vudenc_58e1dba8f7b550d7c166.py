def zmi_manage_css(self, *args, **kwargs):...
"""docstring"""
request = self.REQUEST
response = request.RESPONSE
response.setHeader('Content-Type', 'text/css')
css = []
for stylesheet in self.getStylesheets():
return '\n'.join(css)
s = stylesheet(self)
s = str(stylesheet)
css.append(
    '/* ######################################################################'
    )
css.append('   ### %s' % stylesheet.absolute_url())
css.append(
    '   ###################################################################### */'
    )
css.append(s)
