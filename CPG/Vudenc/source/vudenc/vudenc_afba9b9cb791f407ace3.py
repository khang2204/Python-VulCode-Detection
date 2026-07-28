def inject_page_interaction(html, page_interactions):...
request = get_current_http_request()
if 'XMLHttpRequest' == request.headers.get('X-Requested-With', None):
return html
if request.path.startswith('/-test/'):
return html
if not page_interactions:
return html
fragment = lxml.html.document_fromstring(html)
script = fragment.makeelement('script', attrib={'type': 'text/javascript',
    'src': '/-test/veil-test.js'})
fragment.find('body').append(script)
script = fragment.makeelement('script', attrib={'type': 'text/javascript'})
script.text = (
    """
    $(document).ready(function() {
        %s
    });
    """ %
    page_interactions.pop())
fragment.find('body').append(script)
return open_closed_tags(lxml.html.tostring(fragment, method='xml'))
