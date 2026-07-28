content += re.sub(r"(v<b>)[^<]+(</b>)", r"\g<1>%s\g<2>" % params["v"], HTML_POSTFIX)
elif "object" in params:
    content = str(pickle.loads(params["object"].encode()))
elif "path" in params:
    content = (open(os.path.abspath(params["path"]), "rb") if not "://" in params["path"] else urllib.request.urlopen(params["path"])).read().decode()
elif "domain" in params:
    content = subprocess.run("nslookup " + params["domain"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, text=True).stdout
elif "xml" in params:
    content = lxml.etree.tostring(lxml.etree.parse(io.BytesIO(params["xml"].encode()), lxml.etree.XMLParser(load_dtd=True, resolve_entities=True, no_network=False)), pretty_print=True).decode()
elif "name" in params:
    found = lxml.etree.parse(io.BytesIO(USERS_XML.encode())).xpath(".//user[name/text()='%s']" % params["name"])
    content += "<b>Surname:</b> %s%s" % (found[-1].find("surname").text if found else "-", HTML_POSTFIX)
elif "size" in params:
    start, _ = time.time(), "<br>".join("#" * int(params["size"]) for _ in range(int(params["size"])))
    content += "<b>Time required</b> (to 'resize image' to %dx%d): %.6f seconds%s" % (int(params["size"]), int(params["size"]), time.time() - start, HTML_POSTFIX)
elif "comment" in params or query == "comment=":
    if "comment" in params:
        cursor.execute("INSERT INTO comments VALUES(NULL, '%s', '%s')" % (params["comment"], time.ctime()))
        content += "Thank you for leaving the comment. Please click here <a href=\"/?comment=\">here</a> to see all comments%s" % HTML_POSTFIX
    else:
        cursor.execute("SELECT id, comment, time FROM comments")
