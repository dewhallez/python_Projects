#!/usr/bin/env python3
from pytube import YouTube

url = input("Enter your Youtube video url:  ")
youtube_obj = YouTube(url)
print(youtube_obj.streams)


#video = youtube.streams.first()

#video.download()


#video.streams.all()
#stream = video.streams.all()
#for i in stream:
#    print(i)

