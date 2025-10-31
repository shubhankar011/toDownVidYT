# Downloads YouTube videos with subtitles using yt_dlp 
import yt_dlp
import os

def yt_iops(url, output, path, name=None, choice_index=0):
    yt_opts = {
        'verbose': True,
        'format': output[choice_index],
        'writesubtitles': True,
        'subtitleslangs': ['en'],
        'retries': 10,
        'merge_output_format': 'mp4',
        'outtmpl': f"{path}/%(title)s.%(ext)s" if not name else f"{path}/{name}.%(ext)s",
        'ffmpeg_location': r'C:\ffmpeg\bin'
    }

    cookie_path = os.path.join(os.path.dirname(__file__), 'cookies.txt')
    if os.path.exists(cookie_path):
        yt_opts['cookiefile'] = cookie_path

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])

