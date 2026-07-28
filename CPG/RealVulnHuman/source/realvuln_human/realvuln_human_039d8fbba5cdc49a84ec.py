# Update the user's profile picture ID in the database
                cursor.execute("UPDATE users SET profile_picture = ? WHERE id = ?", (profile_picture_id, user_id))
                conn.commit()
                return {'message': f'Profile picture updated successfully for user {username}'}, 200
            else:
                return {'error': 'User not found'}, 404
        else:
            return {'error': 'Invalid image format'}, 400
    else:
        return {'message': 'Failed to fetch the picture from the provided URL'}, 400
except Exception as e:
    return {'message': str(e)}, 500
