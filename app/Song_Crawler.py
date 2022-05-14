#This python script is used to download the required information about the songs using the spotify API.
#Using this function we download a single JSON file that contains all the information we want.
#This script runs once to create the "database", it does not need to run everytime the application runs.

import spotipy
import subprocess

from spotipy.oauth2 import SpotifyClientCredentials

import pandas as pd

#function which helps us run terminal commands within the script
def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

#spotify API credentials declaration
cid = '8373b95721104a1abd59128c28136059'
secret = 'd9f87ebfcb12449c99d436a6d3e09c67'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#choosing the desired playlist and extracting the URI from its URL address
playlist_link = "https://open.spotify.com/playlist/1YzHgIzS7D30Ex2gGEaNJC"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]


#for loop from track 19 to track 29 to extract the necessary track data
for track in sp.playlist_tracks(playlist_URI)["items"][19:29]:
	#preview URL
	track_preview_url = track["track"]["preview_url"]
    
	#main artist name
	artist_name = track["track"]["artists"][0]["name"]

	#track name
	#some string manipulation to get the desired track_name for our file output
	track_name = track["track"]["name"]
	track_name = track_name.replace("-", "")
	track_name = track_name.replace("(", "")
	track_name = track_name.replace(")", "")
	track_name = track_name.replace("'", "")

	name = (artist_name+"-"+track_name)
			
	name = name.replace(" ", "_")
	
	#calling runcmd function to download track_preview_url for each song and save it as "track_name".mp3 via wget command
	if (track_preview_url):
		print(name)
		runcmd("wget " + track_preview_url + " -O /home/jonwicked/Downloads/Karudis/fingerprint_prototype/python/"+name+".mp3",verbose = True)



