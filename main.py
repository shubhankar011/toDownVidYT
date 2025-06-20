import yt_dlp 
import os

def yt_iops(url, output, path, name):

    print(output)
    choose = int(input("Enter the index of the suitable option: "))

    yt_opts = {
        'verbose' : False,
        'format' : f'{output[choose]}',
        'download_Sections': [{
        'section': {
                'start_time': 2,
                'end_time': 30
            }
        }],
        'writesubtitles': True,
        'subtitleslangs': ['en'],
        'retries':10,
        'cookiefile':'D:/Programming Files/New Folder/python/cookies.txt',
        'outtmpl': f"{path}/{name}.%(ext)s",
        'ffmpeg_location': 'C:/ffmpeg/bin',
        'postprocessors': [{
            'key':'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        },
        {
            'key':'FFmpegEmbedSubtitle'
        }
        ]
    }

    if name == "" or name == None:
        yt_opts['outtmpl'] = f'/{path}/%(title)s.%(ext)s'
    else:
        yt_opts['outtmpl'] = f'/{path}/{name}.%(ext)s'
    try:    
        ydl = yt_dlp.YoutubeDL(yt_opts)
        ydl.download(f"{url}")
        
    except:
        print("Sorry, Unable to download")
        
if __name__ == "__main__":

    url = input("Enter URL: ")
    output = ["bestaudio+bestvideo","bestaudio","bestvideo","best"]
    path = input("Enter the path of the directory in which you want to download the video: ")
    i = 0
    name = None

    if 'playlist' in url or '@' in url:
        print("The given url is of a playlist or a channel, but we will proceed it.")
        i = 1
    else:
        i = 0
    
    if i == 1:
        name = None
    else: 
        name = input("Enter the name of the video or just enter for the default video name")
        name = name.strip()

    if not os.path.exists(path):
        os.makedirs(path)

    yt_iops(url, output, path, name)
