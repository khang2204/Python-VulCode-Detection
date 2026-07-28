<h1> Hello Folks!Are you searching for ip address?Just write and search.</h1>
             <p><h3>Enter address to lookup</h3></p>
             <p><input type = 'text' name = 'address'/></p>
             <p><input type = 'submit' value = 'Lookup'/></p>
          </form>
       </body>
       <a href="dashboard">Go back</a>
    </html>
    """
#XXE    
@app.route('/xml', methods = ['POST', 'GET'])
def xml():
    parsed_xml = None
    if request.method == 'POST':
        xml = request.form['xml']
        parser = etree.XMLParser(no_network=False, dtd_validation=True)
        try:
            doc = etree.fromstring(str(xml), parser)
            parsed_xml = etree.tostring(doc)
        except:
           pass
    return """
    <html>
    <title>xml</title
    <link rel= "stylesheet" type= "text/css" href="/static/styles/board.css"">
       <body><h1> Do you like to plays with markup?</h1>
       <h1> Give us your code we will design for you.</h1>
       """ + "Result:\n<br>\n" + (parsed_xml)  if parsed_xml else "" + """
          <form action = "/xml" method = "POST">
             <link rel= "stylesheet" type= "text/css" href="/static/styles/board.css"">
             <h1> Do you like to play with markup?</h1>
       <h1> Give us your code we will design for you.</h1>
             <p><h3>Enter xml to parse</h3></p>
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
