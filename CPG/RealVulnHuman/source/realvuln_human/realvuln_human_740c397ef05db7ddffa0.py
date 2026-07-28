def custom_hash(password):
    """
    Weak password hashing function using MD5.

    Args:
    - password: The password to hash.

    Returns:
    - The hashed password.
    """
    return hashlib.md5(password.encode()).hexdigest()

# Get user profile from database
def get_user_details_from_database(user_id):
    # Query the database for the user using parameterized query
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE id = ?"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
    return user
