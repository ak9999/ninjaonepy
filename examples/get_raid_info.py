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
    # Get drives and controllers as Python dictionaries
    drives = client.get_raid_drives()
    controllers = client.get_raid_controllers()
    # For this example, we're just going to convert the dictionaries to JSON and write them to a file.
    drives = json.dumps(drives)
    controllers = json.dumps(controllers)
    # Now we can write the drives and raid controllers to JSON files.
    with open('drives.json', 'w', newline='') as f:
        print(drives, file=f)

    with open('controllers.json', 'w', newline='') as f:
        print(controllers, file=f)
