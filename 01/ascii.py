import os
import time
import shutil
import numpy as np
import imageio
from PIL import Image
import yt_dlp

# ASCII characters from dark to light
ASCII_CHARS = "@%#*+=-:. "

# Fixed video URL (no user input)
VIDEO_URL = "https://youtu.be/vgwMsYpblI0"
VIDEO_FILE = "input.mp4"

def download_video(url, filename):
    """Download only video (no audio merge -> no ffmpeg needed)."""
    ydl_opts = {
        'outtmpl': filename,
        'format': 'mp4[ext=mp4][vcodec!=none]',  # only pure mp4 stream
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"[+] Downloaded video as {filename}")

def frame_to_ascii(frame, width):
    """Convert a single frame to ASCII string."""
    img = Image.fromarray(frame).convert('L')
    aspect_ratio = img.height / img.width
    new_height = int(aspect_ratio * width * 0.55)
    img = img.resize((width, new_height))
    pixels = np.array(img)
    # Scale pixel values to ASCII chars
    ascii_str = "".join(
        ASCII_CHARS[min(9, pixel // 25)] for pixel in pixels.flatten()
    )
    ascii_img = "\n".join(
        ascii_str[i:i+width] for i in range(0, len(ascii_str), width)
    )
    return ascii_img

def main():
    # Download video automatically
    download_video(VIDEO_URL, VIDEO_FILE)

    # Get terminal width safely
    columns = shutil.get_terminal_size((80, 20)).columns
    width = max(20, min(columns, 120))

    # Open video and get the perfext frames
    reader = imageio.get_reader(VIDEO_FILE)
    fps = reader.get_meta_data().get('fps', 24)
    delay = 1.0 / fps

    print("[+] Playing ASCII video... Press Ctrl+C to stop.")
    try:
        for frame in reader:
            ascii_img = frame_to_ascii(frame, width)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_img)
            time.sleep(delay)
    finally:
        reader.close()
        # Delete video after playback
        if os.path.exists(VIDEO_FILE):
            os.remove(VIDEO_FILE)
            print(f"[+] Deleted {VIDEO_FILE}")

if __name__ == "__main__":
    main()
