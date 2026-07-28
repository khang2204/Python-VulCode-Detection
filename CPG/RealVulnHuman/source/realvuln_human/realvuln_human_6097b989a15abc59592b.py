setup_db()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/login")


@app.errorhandler(404)
def page_not_found(error):
    detailed_message = render_template_string(
        f"{error}. Requested URL was {request.path}"
    )
    return render_template("404.html", detailed_message=detailed_message)
