@app.route('/evaluate', methods = ['POST', 'GET'])
#Code Injection
def evaluate():
    expression = None
    if request.method == 'POST':
        expression = request.form['expression']
    return """
    <html>
       <link rel= "stylesheet" type= "text/css" href="/static/styles/board.css"">
       <body>""" + "Result: " + (str(eval(expression)).replace('\n', '\n<br>')  if expression else "") + """
          <form action = "/evaluate" method = "POST">
             <h1> Hello Folks! Give us your problem. We will provide you the best mathematical solution. </h1>
             <p><h3>Enter expression to evaluate</h3></p>
             <p><input type = 'text' name = 'expression'/></p>
             <p><input type = 'submit' value = 'Evaluate'/></p>
          </form>
       </body>
       <a href="dashboard">Go back</a>
    </html>
    """
