from pytube import Playlist

# Replace 'your_playlist_url' with the URL of the YouTube playlist you want to download.
playlist_url = 'https://www.youtube.com/playlist?list=....'

# Create a Playlist object
playlist = Playlist(playlist_url)

# Iterate through the videos in the playlist and download each one
for video in playlist.videos:
    try:
        # Download the video in the highest available resolution
        video.streams.get_highest_resolution().download()
        print(f"Downloaded: {video.title}")
    except Exception as e:
        print(f"Error downloading {video.title}: {str(e)}")

print("Download complete.")
