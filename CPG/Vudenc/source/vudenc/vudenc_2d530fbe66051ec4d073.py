def _output_html(complete_output, categories):...
"""docstring"""
return """<html>
    <head>
      <title>Automatically generated keywords by bibclassify</title>
    </head>
    <body>
    {0}
    </body>
    </html>""".format(
    _output_text(complete_output).replace('\n', '<br>')).replace('\n', '')
