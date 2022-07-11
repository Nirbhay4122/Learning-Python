# Importing necessary packages
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter.ttk import *
from tkinter import ttk


window = Tk()
window.geometry("500x500+350+100")
# w=500
# h=500
# ws = window.winfo_screenwidth()
# hs = window.winfo_screenheight()
# x = (ws/2) - (w/2)    
# y = (hs/2) - (h/2)
# window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.resizable(False,False)
window.title("YTVD")
window.config(bg = "gray3")

# Defining function for choosing path or file location
directory = ""
def choose_path():
    file_name.config(text = "")
    file_size.config(text = "")
    file_loc.config(text = "")
    directory = filedialog.askdirectory()
    download_path.set(directory)

# Defining a function for downloading file in the software
def Download():
    url = link_entry.get()
    Selected = options_type.get()

    download_folder = download_path.get()

    if len(url) < 1:
        link_error.config(text = "Please Enter an URL...")
    else:
        file_dd.config(text = "Wait While Your File is Downloading", 
                font = ("varadana",10))

    if len(download_folder) < 1:
        path_error.config(text = "Choose Path...")
    else:
        link_error.config(text = "")
        path_error.config(text = "")
        try:
            Yt = YouTube(url)
            try:
                if(Selected == options[0]):
                    typ = Yt.streams.get_highest_resolution()
                
                elif(Selected == options[1]):
                    typ = Yt.streams.filter(progressive=True, file_extension="mp4").last()

                elif(Selected == options[2]):
                    typ = Yt.streams.filter(only_audio=True)

                try:
                    typ.download(download_folder)
                    link_entry.delete(0, "end")
                    path_holder.delete(0, "end")
                    file_dd.config(text = "File Downloaded Succesfully", font = (12))

                    name = typ.title
                    size = typ.filesize/1024000
                    size = round(size, 2)
                    file_name.config(text = "File Name : "+name)
                    file_size.config(text = "File Size : "+str(size)+"MB")
                    file_loc.config(text = "File Location : "+download_folder)
                except:
                    file_dd.config(text = "Download Failed ", font = (12))
            except:
                file_dd.config(text = "Download Failed", font = (12))
        except:
            path_error.config(text = "Choose Valid Path...", font = (12))




# Heading of the software
heading = Label(window, text = "YouTube video Downloader - Made By Nirbhay Singh", background="gray3", 
            foreground = "#cccc00", font = ("varadana",9,"bold"))
heading.place(x = 60, y = 5)

# URL Lable  For YTVD
url_lable = Label(window, text = "Enter URL :", background="#E8D579", 
                foreground = "black", font = ("varadana",10,"bold"))
url_lable.pack(anchor = "nw", padx = 10, pady = 45)

# URL Entry for ytvd
entry_url = StringVar()
link_entry = Entry(window, width = 45, textvariable = entry_url)
link_entry.place(x = 120, y = 43)
link_error = Label(window, background="gray3", 
                foreground = "#ff6666", font = ("varadana",10,"bold"))
link_error.place(x = 310, y = 73)

# Choose Path for YTVD
# path = Label(window, text = "Path :", background="#E8D579", 
#             foreground = "black", font = ("varadana",10,"bold"))
# path.pack(anchor = "nw", padx = 10)



download_path = StringVar()
path_holder = Entry(window, width = 40, textvariable = download_path)
path_holder.place(x = 10, y = 111)



# path button & its style
path_style = ttk.Style()
path_style.configure("PT.TButton", background = "white", foreground = "black", font = ("varadana",10,"bold"))
path_btn = Button(window, width = 14, text = "Choose Path", style = "PT.TButton", command = choose_path)
path_btn.place(x = 350, y = 110)

# Path Error in software
path_error = Label(window, background="gray3", 
                foreground = "#ff6666", font = ("varadana",10,"bold"))
path_error.place(x = 220, y = 140)

# Choose download type in the software
download_type = Label(window, text = "Download Type :", background="#E8D579", 
                    foreground = "black", font = ("varadana",10,"bold"))
download_type.pack(anchor = "w", padx = 10, pady = 73.3)

options = ["High Quality", "Low Quality", "Audio"]
options_type = ttk.Combobox(window, values = options, width = 25)
options_type.current(0)
options_type.place(x = 150, y = 185)

choose_type = Label(window, text = "Choose Type", background="#E8D579", 
                    foreground = "black", font = ("varadana",10,"bold"))
choose_type.place(x = 383, y = 187)

# Design of Download Button
download_style = ttk.Style()
download_style.configure("DD.TButton", background = "white", foreground = "black", font = ("varadana",10,"bold"))
download_btn = Button(window, width = 50, text = "Download", style = "DD.TButton", command = Download)
download_btn.pack(anchor = "center")

#File Download location and size for software
file_dd = Label(window, background="gray3", 
                foreground = "#ff6666", font = ("varadana",10))
file_dd.pack(anchor = "center",padx = 10, pady = 10)

file_name = Label(window, text = "File Name : ", background="gray3", foreground = "#cccc00", font = ("varadana",10,"bold"))
file_name.pack(anchor = "nw",padx = 10, pady = 10)

file_size = Label(window, text = "File Size : ", background="gray3", foreground = "#cccc00", font = ("varadana",10,"bold"))
file_size.pack(anchor = "nw",padx = 10, pady = 10)

file_loc = Label(window, text = "File Location : ", background="gray3", foreground = "#cccc00", font = ("varadana",10,"bold"))
file_loc.pack(anchor = "nw",padx = 10, pady = 10)

window.mainloop()





