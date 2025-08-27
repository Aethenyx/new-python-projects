import yt_dlp
import os

def download_with_ytdlp():
    url = input("Enter YouTube URL: ")
    output_path = os.path.join(os.path.expanduser('~'), 'Downloads/%(title)s.%(ext)s')
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    download_with_ytdlp()