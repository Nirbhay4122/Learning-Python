# Importing necessary packages
from tkinter import *
from pytube import YouTube
import validators
from tkinter import filedialog
from tkinter import Tk  

from tkinter import ttk
  
# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():
    link_label = Label(root, 
                       text="YouTube link  :",
                       bg="#E8D579")
    link_label.grid(row=1,
                    column=0,
                    pady=5,
                    padx=5)
   
    root.linkText = Entry(root,
                          width=55,
                          textvariable=video_Link)
    root.linkText.grid(row=1, 
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan = 2)
   
    destination_label = Label(root, 
                              text="Destination    :",
                              bg="#E8D579")
    destination_label.grid(row=2,
                           column=0,
                           pady=5,
                           padx=5)
   
    root.destinationText = Entry(root,
                                 width=40,
                                 textvariable=download_Path)
    root.destinationText.grid(row=2, 
                              column=1,
                              pady=5,
                              padx=5)
   
    browse_B = Button(root, 
                      text="Browse",
                      command=Browse,
                      width=12,
                      bg="#05E8E0")
    browse_B.grid(row=2,
                  column=2,
                  pady=1,
                  padx=1)
   
    Download_B = Button(root,
                        text="Download", 
                        command=Download, 
                        width=25,
                        bg="#05E8E0")
    Download_B.place(x = 351, y = 78)
    # Making options to choose quality
    options_label = Label(root, 
                              text="     Quality      :",
                              bg="#E8D579")
    options_label.grid(row=3,
                           column=0,
                           pady=5,
                           padx=5)
    options = ["Choose Quality", "High Quality", "Low Quality", "Audio"]
    options_type = ttk.Combobox(root, values = options, width = 24)
    options_type.current(0)
    options_type.place(x = 115, y = 80)
  
# Defining Browse() to select a 
# destination folder to save the video
  
def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir 
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
   
    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)
  
# Defining Download() to download the video
def Download():      
    # getting user-input Youtube Link
    Youtube_link = video_Link.get()
      
    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()
   
    # Creating object of YouTube()
    getVideo = YouTube(Youtube_link)
   
    # Getting all the available streams of the
    # youtube video and selecting the first
    # from the
    videoStream = getVideo.streams.first()
   
    # Downloading the video to destination 
    # directory
    videoStream.download(download_Folder)
   
    # Displaying the message
    Message.showinfo("SUCCESSFULLY", 
                        "DOWNLOADED AND SAVED IN\n" 
                        + download_Folder)
  
# Creating object of tk class
root = Tk()
   
# Setting the title, background color 
# and size of the tkinter window and 
# disabling the resizing property
root.geometry("600x120")
root.resizable(False, False)
root.title("YouTube_Video_Downloader")
root.config(background="#000000")
   
# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()
   
# Calling the Widgets() function
Widgets()
   
# Defining infinite loop to run
# application
root.mainloop()