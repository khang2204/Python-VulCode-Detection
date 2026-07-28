sandboxes = Blueprint('sandboxes', __name__, template_folder='templates')


@sandboxes.route('/unsafe_params')
def unsafe_params():
    """Renders a page with XSS flags enabled to use browser-based defenses"""
    title = 'Unsafe Parameters'
    description = 'A GET parameter is unsafely handled. Try entering something in the text box, or setting ' \
                  '"?name=something" in the header'

    name = request.args.get('name', 'world!')
    return render_template('sandboxes/unsafe_params.html', name=name, title=title, description=description)


unsafe_cookies = Blueprint('unsafe_cookies', __name__)


@sandboxes.route('/unsafe_cookies', methods=["GET", "POST"])
def unsafe_cookies():
    """Renders a page that processes cookies in an unsafe way"""
    title = 'Unsafe Cookies'
    description = 'A cookie called "name" is unsafely handled. Try setting it using a cookie editor, or by enter a ' \
