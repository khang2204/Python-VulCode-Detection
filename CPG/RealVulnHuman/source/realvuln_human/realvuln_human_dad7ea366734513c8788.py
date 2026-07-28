<a href="dashboard">Go back</a>
    </html>
    """


# server side template injection
@app.route('/sayhi', methods = ['POST', 'GET'])
def sayhi():
   name = ''
   if request.method == 'POST':
      name = '<br>Hello %s!<br><br>' %(request.form['name'])

   template = """
   <html>
      <body>
         <link rel= "stylesheet" type= "text/css" href="/static/styles/board.css"">
         <form action = "/sayhi" method = "POST">
            <p><h3>Tell us your name and we want to send you greetings!</h3></p>
            <p><input type = 'text' name = 'name'/></p>
            <p><input type = 'submit' value = 'Submit'/></p>
         </form>
