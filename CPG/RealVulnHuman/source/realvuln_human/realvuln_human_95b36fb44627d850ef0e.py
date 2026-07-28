if totp.verify(otp):
        libmfa.mfa_enable(g.session['username'])
        return redirect('/mfa/')
    else:
        flash("The OTP was incorrect")
        return redirect('/mfa/')

    return render_template('mfa.enable.html')


@mod_mfa.route('/disable', methods=['GET'])
def do_mfa_disable():

    if 'username' not in g.session:
        return redirect('/user/login')

    libmfa.mfa_disable(g.session['username'])
    return redirect('/mfa/')
