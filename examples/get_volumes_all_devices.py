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
    # Get a list of volumes for all devices as Python dictionaries
    volumes = client.get_volumes()
    # For this example, we're just going to convert the dictionaries to JSON and write them to a file.
    volumes = json.dumps(volumes)
    # Now we can write the results to a JSON file.
    with open('volumes.json', 'w', newline='') as f:
        print(volumes, file=f)
