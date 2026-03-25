import ninjaonepy
import os
import json

# Create our client using OAuth2 credentials
# Assuming we are storing our credentials in environment variables we can access
client_id = os.environ.get('NINJA_CLIENT_ID')
client_secret = os.environ.get('NINJA_CLIENT_SECRET')
if not client_id or not client_secret:
    raise ValueError('NINJA_CLIENT_ID and NINJA_CLIENT_SECRET environment variables are required')

with ninjaonepy.Client(
    client_id=client_id,
    client_secret=client_secret,
    europe=False
) as client:
    # Get usernames and logon times for all devices as Python dictionaries
    logged_on_users = client.get_last_logged_on_users()
    # For this example, we're just going to convert the dictionaries to JSON and write them to a file.
    logged_on_users = json.dumps(logged_on_users)
    # Now we can write the results to a JSON file.
    with open('logged_on_users.json', 'w', newline='') as f:
        print(logged_on_users, file=f)
