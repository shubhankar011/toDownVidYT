import yt_dlp
from yt_dlp import YoutubeDL
import vlc
import os

# Defining name and folder/path of file
print("Try Using for e.g. : 'C://User//PC//Videos' or just 'Video'")
dir = input("Enter the folder/path to save the file: ")
if not os.path.exists(dir):
    os.makedirs(dir)
name = input("Name of the file: ")
# name = name+'.mp4' 
print("For audio-only - 'a'//0, video-only - 'v'//1, video with both in hiqh quality - 'hva', both in low quality - 'sva'")
select = input("Enter the type of video:")

#Defining Progress Hook
def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} at {d['_speed_str']}")
        
#Making a Well Message for the user
class Logger_error:
    def debug(self, msg):
        print("Downloading...",msg)
    
    def warning(self, msg):
        print(f'The Warning is: {msg}')
    
    def error(self, msg):
        print(f'The Error is: {msg}')


# Seleting Configuration (yt_opts is a dictionary which has configurations to set)
yt_opts = {
    'verbose': True,
    'download_sections': [{
        'section': {
            'start_time': 2,
            'end_time': 30
        }
    }],
    #'format': 'bestaudio+bestvideo/best', -- Use this if you've downloaded and installed FFmpegVideoConvertor
    'format': 'best',
    'outtmpl': f'{dir}/{name}',
    'progress_hook': [progress_hook],
    'logger': Logger_error(),
    'writesubtitles': True,
    'subtitleslangs': ['en'],
    'postprocessors': [{
        'key':'FFmpegVideoConvertor',
        'preferedformat':'mp4'
    }]

}
# Asking URL of a specific video, dont give url of a playlist
urlOfVideo = input("Enter the url: ")

# Making format according to the file
if select == 'a' or select == '0':
    yt_opts['format'] = 'bestaudio'

elif select == 'v' or select == '1':
    yt_opts['format'] = 'bestvideo'

elif select=='hva' or select=='2':
    yt_opts['format'] = 'bestaudio+bestvideo/best'

elif select == 'sva' or select =='3':
    yt_opts['format'] = 'best'

with YoutubeDL(yt_opts) as ydl:
    #Info of Video if you don't want comment the below 2 lines
    info = ydl.extract_info(urlOfVideo, download=False)
    # print(info)
    file_extension = info.get('ext')
    ydl.download(urlOfVideo)

# Downloading Video
with YoutubeDL(yt_opts) as ydl:
    #Info of Video if you don't want comment the below 2 lines
    info = ydl.extract_info(urlOfVideo, download=False)
    # print(info)
    file_extension = info.get('ext')
    ydl.download(urlOfVideo)

# If upper downloading code doesn't work then try with this
# ydl = yt_dlp.YoutubeDL(yt_opts)
# info = ydl.extract_info(urlOfVideo, download=False)
# print(info)
# ydl.download(urlOfVideo)

file_path = os.path.abspath(f'{dir}/{name}.{file_extension}

# Playing the media from Windows Media Player
try:
    os.startfile(file_path)

    # Playing the file from VLC Media Player
    player = vlc.MediaPlayer()
    file = vlc.Media(file_path)
    player.set_media(file)
    
    player.play()
    while player.is_playing():
        pass
except:
    print(f'The file couldn't be played automatically. Go through the DIRECTORY - {file_path}')
