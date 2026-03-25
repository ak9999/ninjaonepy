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
    # Get operating systems for all devices as Python dictionaries
    operating_systems = client.get_operating_systems()
    # For this example, we're just going to convert the dictionaries to JSON and write them to a file.
    operating_systems = json.dumps(operating_systems)
    # Now we can write the results to a JSON file.
    with open('os.json', 'w', newline='') as f:
        print(operating_systems, file=f)
