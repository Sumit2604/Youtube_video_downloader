import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox


def createwidgets():

    link_lable = Label(root, text="YouTube URL:", bg="#E8D579")
    link_lable.grid(row=1, column=0, pady=10, padx=7)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1,column=1, pady=10, padx=5 )

    destination_lable = Label(root, text="Destination", bg="#E8D579")
    destination_lable.grid(row=2,column=0,pady=5, padx=5)

    root.destination_link = Entry(root, width=60, textvariable=download_path)
    root.destination_link.grid(row=2, column=1, pady=5, padx=5)

    browse_but = Button(root, text="Browse", command=browse, width=15, bg="#05E8E0")
    browse_but.grid(row=2, column= 2, pady=2, padx= 5)

    download_but= Button(root, text="Download Video", command=download_video, width=20, bg="#05E8E0")
    download_but.grid(row=3, column=1, pady=2 , padx=3)



def browse():

    download_dir= filedialog.askdirectory(initialdir="Your Directory path")
    download_path.set(download_dir)

def download_video():

    url = video_link.get()
    folder = download_path.get()

    get_video= YouTube(url)
    get_stream = get_video.streams.get_highest_resolution()
    get_stream.download(folder)





    messagebox.showinfo("downloded successfully", "You will find your video at\n"+folder)

root = tk.Tk()


root.geometry("600x160")
root.resizable(False,False)
root.title("Youtube Video Downloader")
root.config(background="#000000")


video_link=StringVar()
download_path=StringVar()

createwidgets()

root.mainloop()
