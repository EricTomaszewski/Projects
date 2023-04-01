import sys
import pytube               # for YouTube
import youtube_dl           # for all else (counterintuitively doesn't work on YouTube...)



# PASS THE ARGUMENT FROM FLASK APP & HTML
VideoLink = sys.argv[1]
print(VideoLink)
print(type(VideoLink))


# PARAMETERS FOR youtube_dl
ydl_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",  # choose the best available video and audio format
    "outtmpl": "%(title)s.%(ext)s",  # name the downloaded file as the title of the video with the extension
    "no_call_home": True,  # disable uploader ID extraction
    "verbose": True,  # enable verbose logging
}



try:
    if VideoLink.startswith("https://www.youtube") or VideoLink.startswith("https://youtube") or VideoLink.startswith("https://youtu.be"):
        video = pytube.YouTube(VideoLink)
        stream = video.streams.filter(file_extension='mp4').first()
        filename = f"{video.title}.mp4" 
        stream.download(output_path='./', filename=filename)
    else:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([VideoLink])        
    print("=====##### VIDEO DOWNLOAD FINISHED #####=====")
except:
    print("-----!!!!! SoMeThInG WeNt WrOnG !!!!!-----")
'''try:
    video = pytube.YouTube(VideoLink)
    stream = video.streams.filter(file_extension='mp4').first()
    stream.download(output_path='./', filename='video.mp4')
    print("=====##### VIDEO DOWNLOAD FINISHED #####=====")'''