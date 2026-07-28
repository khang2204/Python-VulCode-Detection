@auth.route('/login/auth')...
if g.user.is_authenticated:
return redirect(url_for('gallery.show_posts'))
callback_url = url_for('auth.oauthorize_callback', next=request.args.get(
    'next'))
return twitter.authorize(callback=callback_url or request.referrer or None)
