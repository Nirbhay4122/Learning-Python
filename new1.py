from tkinter import *
from tkinter.ttk import *
import time

def start():
    MB = 10
    download = 0
    speed = 1
    while(download<MB):
        time.sleep(0.2)
        bar['value']+=(speed/MB)*100
        download+=speed
        percent.set(str(int((download/MB)*100))+"%")
        text.set(str(download)+"/"+str(MB)+" MB completed")
        window.update_idletasks()

window = Tk()
window.geometry("500x200")

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.place(x=100,y=90)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()

window.mainloop()




















# from tqdm import tqdm
# import time
# x = int(input("Enter the progress number : "))
# for x in tqdm(range(x)):
#     time.sleep(1.0)