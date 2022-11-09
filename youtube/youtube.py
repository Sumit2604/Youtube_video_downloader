
from pytube import YouTube

print("Welcome to Y-Downloader")

print()

link=input('enter your link')
#link= "https://www.youtube.com/watch?v=2yLbm8MIpPk&list=PLjVLYmrlmjGfiBKfgOFEbI4FDWvLwYh-e"
youtube_1=YouTube(link)
print(youtube_1.title) 

#videos=youtube_1.streams.filter(only_video=True)
#videos=youtube_1.streams.filter(only_audio=True)

videos=youtube_1.streams.all()

vid= list(enumerate(videos)) 
for i in vid:
    print(i)
print()
quality=int(input('enter no:'))
print("downloading")
videos[quality].download()

print('successfully')

'''
#  *****for downloaing the whole playlist*****
#link="https://www.youtube.com/playlist?list=PLjVLYmrlmjGfSYkgH-_jgC8KMxyRzq7US"

from pytube import Playlist 

print("Welcome to Y-Downloader")

print()

py=Playlist(input("upload your link"))

print("downloading:",py.title)
#print(f'downloading: {py.title}')

for video in py.videos:
    video.streams.get_highest_resolution().download()

print("Downloading done")

'''









