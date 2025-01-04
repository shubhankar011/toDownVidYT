import yt_dlp
from yt_dlp import YoutubeDL
import vlc
import os

name = input("Name of the file: ")
name = name+'.mp4'

# Choosing Options to download
yt_opts = {
    'verbose': False,
    'download_sections': [{
        'section': {
            'start_time': 2,
            'end_time': 7
        }
    }],
    'format': 'best',
    'outtmpl': f'D:/Programming Files/Python Files/YT-DLP/{name}'
}

urlOfVideo = input("Enter the url: ")
ydl = yt_dlp.YoutubeDL(yt_opts)
info = ydl.extract_info(urlOfVideo, download=False)
print(info)
ydl.download(urlOfVideo)

# Playing the media from Windows Media Player
os.startfile(f'D:/Programming Files/Python Files/YT-DLP/{name}')

# Playing the file from VLC Media Player
player = vlc.MediaPlayer()
file = vlc.Media(f'D:/Programming Files/Python Files/YT-DLP/{name}')
player.set_media(file)

player.play()
while player.is_playing():
    pass
