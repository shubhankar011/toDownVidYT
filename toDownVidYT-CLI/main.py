import yt_dlp 
import os

def yt_iops(url, output, path, name):
    print("Available formats:")
    for i, fmt in enumerate(output):
        print(f"{i}: {fmt}")
    
    choose = int(input("Enter the index: "))

    yt_opts = {
        'verbose': False,
        'format': output[choose],
        'writesubtitles': True,
        'subtitleslangs': ['en'],
        'retries': 10,
        'outtmpl': f"{path}/%(title)s.%(ext)s" if not name else f"{path}/{name}.%(ext)s",
        'ffmpeg_location': 'C:/ffmpeg/bin',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }, {
            'key': 'FFmpegEmbedSubtitle'
        }]
    }

    cookie_path = 'D://cookies.txt'
    if os.path.exists(cookie_path):
        yt_opts['cookiefile'] = cookie_path
    
    try:    
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"Download failed: {e}")

if __name__ == "__main__":
    url = input("Enter URL: ")
    output = ["bestaudio+bestvideo", "bestaudio", "bestvideo", "best"]
    path = input("Enter download directory: ")
    path = 'D:/'+path
    name = None
    if 'playlist' not in url and '@' not in url:
        name = input("Enter filename (or press Enter for default): ").strip()
        name = name if name else None
    
    if not os.path.exists(path):
        os.makedirs(path)
    
    yt_iops(url, output, path, name)
