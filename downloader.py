from pytube import YouTube
from tkinter import filedialog
url_input=input("Please Enter Your URL: ")
all_streams=YouTube(url_input).streams.all()
v=-1
for i in all_streams:
    v = v+1
    print(str(v) + " : " + str(i))

stm_input=int(input("Please Choose The Suitable Stream: "))
print("Please Choose Directory To Save :)")
folder_name = filedialog.askdirectory()
choice=all_streams[stm_input].download(folder_name)
print("DOWNLOAD COMPLETED .........")
