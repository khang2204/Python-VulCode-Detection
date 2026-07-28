if book:
        responseObject = {
            'book_title': book.book_title,
            'secret': book.secret_content,
            'owner': book.user.username
        }
        return Response(json.dumps(responseObject), 200, mimetype="application/json")
    else:
        return Response(error_message_helper("Book not found!"), 404, mimetype="application/json")
else:
    user = User.query.filter_by(username=resp['sub']).first()
    book = Book.query.filter_by(user=user, book_title=str(book_title)).first()
    if book:
        responseObject = {
            'book_title': book.book_title,
            'secret': book.secret_content,
            'owner': book.user.username
        }
        return Response(json.dumps(responseObject), 200, mimetype="application/json")
    else:
        return Response(error_message_helper("Book not found!"), 404, mimetype="application/json")
