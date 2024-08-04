# spotify-playlist-downloader
A simple spotify playlist to mp3 converter.

# Spotify to MP3 Downloader

This project allows you to download tracks from a Spotify playlist as MP3 files using the Spotipy library to fetch track information from Spotify and yt-dlp to download the audio from YouTube.

## Features

- Fetches track names and artists from a Spotify playlist.
- Downloads tracks as MP3 files using yt-dlp.
- Supports concurrent downloads to speed up the process.

## Requirements

- Python 3.6+
- Spotipy
- yt-dlp
- ffmpeg (for audio conversion)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/parthlovestech/spotify-to-mp3.git
    cd spotify-to-mp3
    ```

2. **Install the required Python packages:**
    ```bash
    pip install spotipy yt-dlp
    ```

3. **Install ffmpeg:**
    - **Windows:**
      Download and install from [FFmpeg website](https://ffmpeg.org/download.html).
    - **macOS:**
      ```bash
      brew install ffmpeg
      ```
    - **Linux:**
      ```bash
      sudo apt-get install ffmpeg
      ```

## Configuration

1. **Set up Spotify API credentials:**
   - Create a new application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Get your `Client ID` and `Client Secret`.

2. **Update the credentials in the script:**
    ```python
    SPOTIPY_CLIENT_ID = 'your_client_id'
    SPOTIPY_CLIENT_SECRET = 'your_client_secret'
    ```

## Usage

1. **Run the script:**
    ```bash
    python spotify-to-mp3.py
    ```

2. **Follow the prompts:**
   - Enter the Spotify playlist URL.
   - Enter the download path (or press Enter to use the current directory).

3. **The script will:**
   - Fetch the track names from the Spotify playlist.
   - Download the tracks as MP3 files to the specified directory.

## Example

Here's an example of what running the script looks like:

```bash
$ python spotify-to-mp3.py
Enter the Spotify playlist URL: https://open.spotify.com/playlist/your_playlist_id
Enter the download path (or press Enter to use the current directory): ./downloads
Fetching track names...
Downloading tracks...
Download complete.
