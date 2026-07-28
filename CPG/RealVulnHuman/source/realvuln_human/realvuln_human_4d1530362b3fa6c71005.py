<textarea class="input" name="xml" cols="40" rows="5"></textarea>
             <p><input type = 'submit' value = 'Parse'/></p>
          </form>
       </body>
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
      %s
      </body>
      <a href="dashboard">Go back</a>
   </html>
   """ %(name)
   return render_template_string(template)

if __name__ == "__main__":
    app.debug = True
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000)
