import os
import yt_dlp
import vlc
import time
import subprocess


def open_in_vlc(file_path):
    try:
        file_path = os.path.abspath(file_path)
        print(f"\n🎬 Opening file in VLC: {file_path}")
        subprocess.Popen(["vlc", file_path])  # Open full VLC app
    except FileNotFoundError:
        print("VLC not found in PATH. Please make sure VLC is installed and added to PATH.")
    except Exception as e:
        print(f"Error opening VLC: {e}")
# def open_in_vlc(file_path):

#     try:
#         file_path = os.path.abspath(file_path)
#         print(f"\nOpening file in VLC: {file_path}")

#         player = vlc.MediaPlayer(file_path)
#         player.play()

#         while True:
#             state = player.get_state()
#             if state in (vlc.State.Ended, vlc.State.Error):
#                 print("Playback ended or error occurred.")
#                 break
#             time.sleep(1)

#         player.stop()
#     except Exception as e:
#         print(f"Error while opening VLC: {e}")


def yt_iops(url, output, path, name=None, choice_index=0, cookie_path=None):

    os.makedirs(path, exist_ok=True)
    yt_opts = {
        'format': output[choice_index],
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s') if not name else os.path.join(path, f"{name}.%(ext)s"),
        'merge_output_format': 'mp4',
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }
        ],
        # 'progress_hooks': [lambda d: print(f"\r {d.get('status', '')}: {d.get('filename', '')}", end='')]
    }

    cookie_path = os.path.join(os.path.dirname(__file__), 'cookies.txt')
    if os.path.exists(cookie_path):
        yt_opts['cookiefile'] = cookie_path

    try:
        print("\nDownload starting...")
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            output_path = ydl.prepare_filename(info)
            final_path = os.path.splitext(output_path)[0] + ".mp4"

        print(f"\nDownload completed successfully!")
        print(f"Saved at: {final_path}") 
        open_in_vlc(final_path)

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    print("toDownVidYT - YouTube Video Downloader")
    url = input("Enter YouTube URL: ").strip()
    print("\nChoose format:")
    options = ["bestaudio+bestvideo", "bestaudio", "bestvideo", "best"]
    for i, opt in enumerate(options):
        print(f"{i}. {opt}")

    try:
        choice_index = int(input("\nEnter your choice (0–3): "))
        if not (0 <= choice_index < len(options)):
            raise ValueError("Invalid choice index.")
    except ValueError:
        print("Invalid input. Defaulting to 'bestaudio+bestvideo'.")
        choice_index = 0

    path = os.path.join(os.getcwd(), "downloads")
    name = input("Optional filename (press Enter to skip): ").strip() or None

    yt_iops(url, options, path, name, choice_index)
