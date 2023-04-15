from pytube import YouTube

url = "https://www.youtube.com/watch?v=p07ZZZVL72E&t=273s&ab_channel=CodingBunch"


def on_download_progress(stream,chunk,bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded*100 /stream.filesize

    print(f"Download progression {int (percent)} % ")
    

youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)


stream = youtube_video.streams.get_highest_resolution()
print("Downloading")
stream.download()
print("Finished")