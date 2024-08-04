import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp as youtube_dl 
import re
from multiprocessing import Pool

# Spotify API credentials
SPOTIPY_CLIENT_ID = '3f3532f3de454718992cb449f06dcae2'
SPOTIPY_CLIENT_SECRET = '52e6e0bc2237410ba0bd8b64df26b6f5'

# Function to get track names from Spotify playlist
def get_playlist_tracks(playlist_url):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                               client_secret=SPOTIPY_CLIENT_SECRET))
    
    # Extract playlist ID from URL
    match = re.search(r'playlist\/([a-zA-Z0-9]+)', playlist_url)
    if not match:
        raise ValueError("Invalid playlist URL")
    
    playlist_id = match.group(1)
    
    try:
        results = sp.playlist_tracks(playlist_id)
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API error: {e}")
        return []

    tracks = [track['track']['name'] + ' ' + track['track']['artists'][0]['name'] for track in results['items']]
    
    return tracks

# Function to download track as MP3
def download_track(track_name, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/{track_name}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': 192,
        }],
        'noplaylist': True,
        'quiet': True,
        'concurrent_fragment_downloads': 4,  # Increase the number of concurrent downloads
        'fragment_retries': 10,  # Retry downloading fragments if they fail
        'retries': 10,  # Retry downloading the entire file if it fails
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        query = f'{track_name} song'
        try:
            # Use yt-dlp's extract_info to search for the track
            info_dict = ydl.extract_info(f"ytsearch:{query}", download=False)
            if 'entries' in info_dict:
                # Download the first search result
                video = info_dict['entries'][0]
                ydl.download([video['url']])
        except Exception as e:
            print(f"Error downloading track {track_name}: {e}")

# Wrapper function to pass to pool.map
def process_track(args):
    track_name, output_path = args
    download_track(track_name, output_path)

if __name__ == "__main__":
    playlist_url = input("Enter the Spotify playlist URL: ")
    output_path = input("Enter the download path (or press Enter to use the current directory): ")
    if not output_path:
        output_path = '.'
    
    print("Fetching track names...")
    tracks = get_playlist_tracks(playlist_url)
    
    print("Downloading tracks...")
    with Pool(processes=4) as pool:  # Adjust the number of processes based on your system
        pool.map(process_track, [(track, output_path) for track in tracks])
    
    print("Download complete.")
