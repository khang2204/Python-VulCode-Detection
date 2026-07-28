"""
Update the user's profile picture by fetching it from a provided URL.
This endpoint is vulnerable to SSRF, allowing external service interaction.
"""
data = api.payload
username = data['username']
picture_url = data['picture_url']

try:
    # Fetch the picture from the URL provided by the user
    response = requests.get(picture_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Here, instead of actually saving the picture, we'll just simulate that process.
        # Vulnerability point: Fetching content from an arbitrary URL provided by the user
        if 'image/jpeg' in response.headers['Content-Type'] or 'image/png' in response.headers['Content-Type']:

            conn = get_db_connection()
            cursor = conn.cursor()
