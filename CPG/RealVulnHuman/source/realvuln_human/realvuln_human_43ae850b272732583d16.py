def do_lxml_etree_fromstring(user_input):
    return etree.fromstring(user_input)


def do_xml_dom_pulldom_parsestring(user_input):
    return pulldom.parseString(user_input)


def do_xml_sax_parsestring(user_input):
    return sax.parseString(user_input, ContentHandler())
