import yt_dlp

def get_user_input(prompt):
    return input(prompt)

def download_playlist(playlist_url, download_path):
    ydl_opts = {
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'format': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def main():
    playlist_url = get_user_input("Enter the URL of the YouTube playlist: ")
    download_path = get_user_input("Enter the directory to save the videos: ")
    download_playlist(playlist_url, download_path)

if __name__ == "__main__":
    main()
