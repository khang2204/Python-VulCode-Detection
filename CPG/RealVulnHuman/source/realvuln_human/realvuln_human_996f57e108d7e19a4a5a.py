return redirect("/signup")

        session.delete(token)

        if user_already_exists:
            flash("User already exists", 'warning')
            return redirect("/signup")

        user = User(
            form.email.data,
            hashpw(form.password.data.encode('utf-8'), gensalt()).decode())

        session.add(user)
        session.commit()

return redirect('/home')
