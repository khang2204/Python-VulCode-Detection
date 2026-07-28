Message.query.filter_by(id=id).update({
            'acknowledged': True
        })
        db.session.commit()

        return jsonify(API_STATUS_SUCCESS)


class UsersView(FlaskView):
    @admin_required
    def index(self):
        users = [user.serialize for user in User.query.all()]
        ret = {'users': users}
        ret.update(API_STATUS_SUCCESS)
        return jsonify(ret)

    def get(self, id):
        if not is_admin_or_owning_user(id):
            return jsonify(API_STATUS_ERROR)

        user = User.query.filter_by(id=id).first()
        if not user:
            return jsonify(API_STATUS_ERROR)
        ret = {'user': user}
        ret.update(API_STATUS_SUCCESS)
