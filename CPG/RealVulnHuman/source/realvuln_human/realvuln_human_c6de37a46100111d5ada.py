return {'error': 'Invalid username or password'}, 401

@ns.route('/profile')
class UserProfile(Resource):
    @ns.expect(profile_query)
    @ns.response(200, 'Success', user_profile_model)
    @ns.response(400, 'User ID is required')
    @ns.response(404, 'User profile not found')
    #@token_required
    #def get(self, current_user):
    def get(self):
        """
        Retrieves the profile information of a user based on the provided user ID.
        """
        args = profile_query.parse_args()
        user_id = args.get('user_id')

        with get_db_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT username, email, country, role, permissions, team FROM users WHERE id = ?"
            cursor.execute(query, (user_id,))
            user_profile = cursor.fetchone()

        if user_profile:
            return dict(user_profile), 200
        else:
            return {'error': 'User profile not found'}, 404

@ns.route('/update-profile')
class UserProfileUpdate(Resource):
    @api.expect(update_model)
    @api.response(200, 'Profile updated successfully.', response_model)
    @api.response(401, 'Authentication required.')
    @api.response(403, 'Unauthorized to modify other user profiles.')
    def post(self):
        """
        Updates a user profile information.
