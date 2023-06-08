import yt_dlp

# Prompt the user for the URL of the playlist
playlist_url = input("Enter the URL of the YouTube playlist: ")

# Prompt the user for the directory to save the videos
download_path = input("Enter the directory to save the videos: ")

# Set the options for yt-dlp
ydl_opts = {
    'outtmpl': f'{download_path}/%(title)s.%(ext)s',
    'merge_output_format': 'mp4',
    'format': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
}

# Create a yt-dlp object for the playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
