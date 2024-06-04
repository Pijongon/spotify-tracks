import json
import subprocess
import sys

# Check if the JSON file name is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python download_tracks.py <json_file>")
    sys.exit(1)

# Get the input file path from the command-line arguments
input_file_path = sys.argv[1]

# Read the JSON data from the specified file
with open(input_file_path, 'r') as file:
    data = json.load(file)

for item in data:
    # Extract the spotify_track_uri
    track_uri = item.get("spotify_track_uri")
    
    # Check if the track_uri exists and is not empty
    if track_uri:
        # Transform the URI to the desired URL format
        track_id = track_uri.split(':')[-1]
        track_url = f"https://open.spotify.com/track/{track_id}"
        
        # Create the bash command
        bash_command = f"spotdl {track_url}"
        
        # Execute the bash command
        subprocess.run(bash_command, shell=True)

print("All commands have been executed.")
