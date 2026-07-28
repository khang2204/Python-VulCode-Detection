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
