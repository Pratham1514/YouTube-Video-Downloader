from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from pytube import YouTube

import shutil


#Functions
def select_path():
    #allows user to select path from file explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading......")
    #download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Download Complete!!!... Download Another Video....")



screen =Tk()
title = screen.title("YT Video Downloader")
icon = screen.iconbitmap(r"movie.ico")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file="yt.png")
#resize
logo_img = logo_img.subsample(2,2)

canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download Link : ", font=("Arial", 15))

#Select path for file saving
path_label = Label(screen, text="Select Path for Download Video", font=("Arial",15))
select_btn = Button(screen, text="Select", command=select_path)

#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)


#Add widgets to the window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download button
download_btn = Button(screen, text="Download File", command=download_file)

#Add to canvas
canvas.create_window(250, 390, window=download_btn)


screen.mainloop()