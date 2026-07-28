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
