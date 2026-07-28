@ns.route('/delete-user/<int:user_id>')
@ns.doc(description='Delete a user from the database without proper authorization checks. '
                    'This endpoint represents a Broken Function Level Authorization vulnerability.',
       responses={200: ('User successfully deleted', delete_model),
                  404: ('User not found', error_model)})
class UserDelete(Resource):
    #@token_required
    #def delete(self, current_user, user_id):
    def delete(self, user_id):
        """
            Delete a user from the application.
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()
            if user:
                cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
                conn.commit()
                response = make_response(jsonify({'message': 'User deleted successfully'}), 200)
                return response
            else:
                response = make_response(jsonify({'error': 'User not found'}), 404)
                return response

@ns.route('/update_picture')
class ProfilePicture(Resource):
    @api.expect(profile_pic_model)
    def post(self):
        """
        Update the user's profile picture by fetching it from a provided URL.
        This endpoint is vulnerable to SSRF, allowing external service interaction.
        """
        data = api.payload
