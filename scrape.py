from yt_dlp import YoutubeDL


video_url = "https://www.youtube.com/watch?v=mDveiNIpqyw"
opts = dict()

with YoutubeDL(opts) as yt:
    info = yt.extract_info(video_url, download=False)
    video_title = info.get("title", "")
    width = info.get("width", "")
    height = info.get("height", "")
    language = info.get("language", "")
    print(video_url, video_title, width, height, language)