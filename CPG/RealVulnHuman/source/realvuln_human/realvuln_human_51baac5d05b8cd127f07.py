return redirect("/")


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/is_logged_in', methods=['GET'])
def logged_in():
    return {
        'is_logged_in': current_user.is_authenticated,
        'username':
        current_user.email if current_user.is_authenticated else '-'
    }
