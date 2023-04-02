from flask import Flask, render_template, request, Response
# import subprocess
import pytube               # for YouTube
import youtube_dl           # for all else (counterintuitively doesn't work on YouTube...)

import sys                  # for Thread



# PARAMETERS FOR youtube_dl
ydl_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",  # choose the best available video and audio format
    "outtmpl": "%(title)s.%(ext)s",  # name the downloaded file as the title of the video with the extension
    "no_call_home": True,  # disable uploader ID extraction
    "verbose": True,  # enable verbose logging
}



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/download', methods=['POST'])
def download_video():
    VideoLink = request.form['VideoLink']
    
    def progress_function(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        progress = bytes_downloaded / total_size * 100
        result = f"Downloaded {bytes_downloaded} out of {total_size} bytes ({progress:.2f}%)"
        # Send the result as a server-sent event
        yield f"data: {result}\n\n"
        
    # Open a server-sent event stream
    response = Response(progress_function(stream, 0, stream.filesize), mimetype='text/event-stream')
    # Start the download process in a background thread
    thread = Thread(target=stream.download, kwargs={'output_path': './', 'filename': filename})
    thread.start()
    
    try:
        if VideoLink.startswith("https://www.youtube") or VideoLink.startswith("https://youtube") or VideoLink.startswith("https://youtu.be"):
            video = pytube.YouTube(VideoLink)
            stream = video.streams.filter(file_extension='mp4').first()
            filename = f"{video.title}.mp4" 
            stream.download(output_path='./', filename=filename)
            output = f"Video downloaded successfully as {filename}"
        else:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([VideoLink])        
            output = "Invalid downloaded successfully."
    except:
        output = "Error occurred while downloading video"
    
    # Return the result as a plain text response
    return output



if __name__ == '__main__':
    # app.run(debug=True)
    app.run()