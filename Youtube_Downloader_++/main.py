import tkinter
import customtkinter
from pytube import YouTube
from time import sleep

def verify():
    value = chooseCategory.get()
    if value == "mp3(audio)":
        startaudiodownload()
    elif value == "mp4(audio and video)":
        startvideodownload()
def startaudiodownload():
    test = False
    try:
        ytLink = link.get()
        ytobject = YouTube(ytLink, on_progress_callback=on_progress)
        print(ytLink)
        audio = ytobject.streams.get_audio_only()
        audio.download("./audio_files")
        test = True


        
        
    except:
        print("EROR")
    if test == True:    
        finished_label.configure(text="Audio Succefully Downloaded")
        sleep(7)
        pPercentage.configure(text="0%")
        pPercentage.update()
        pProgressbar.set(0)
        pProgressbar.update()
        finished_label.configure(text="")
        finished_label.update()
    else:
        finished_label.configure(text="ERROR the link is wrong or the program run into an error.")
        sleep(7)
        pPercentage.configure(text="0%")
        pPercentage.update()
        pProgressbar.set(0)
        pProgressbar.update()
        finished_label.configure(text="")
        finished_label.update()

def startvideodownload():
    test = False
    try:
        ytLink = link.get()
        ytobject = YouTube(ytLink, on_progress_callback=on_progress)
        print(ytLink)
        audio = ytobject.streams.get_highest_resolution()
        audio.download("./audio_files")
        test = True


        
        
    except:
        print("EROR")
    if test == True:    
        finished_label.configure(text="Audio Succefully Downloaded")
        sleep(7)
        pPercentage.configure(text="0%")
        pPercentage.update()
        pProgressbar.set(0)
        pProgressbar.update()
        finished_label.configure(text="")
        finished_label.update()
    else:
        finished_label.configure(text="ERROR the link is wrong or the program run into an error.")
        sleep(7)
        pPercentage.configure(text="0%")
        pPercentage.update()
        pProgressbar.set(0)
        pProgressbar.update()
        finished_label.configure(text="")
        finished_label.update()





def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()
    pProgressbar.set(float(percentage_of_completion) / 100)
    pProgressbar.update()
    




#System settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("Hades.json")



#Our App Frame
app = customtkinter.CTk()
app.geometry("500x350")
app.title("Youtube Downloader ++")
app.wm_iconbitmap('youtube_downloader_++.ico')


#Adding ui Elements
title1 = customtkinter.CTkLabel(app, text="Youtube Downloader ++")
title1.pack(padx=10, pady=10)

chooseCategory = customtkinter.CTkComboBox(master=app,
                                     values=["mp3(audio)", "mp4(audio and video)", ],
                                     font=("Segoe UI", 15, "bold")
)
chooseCategory.pack()
chooseCategory.set("Select Format")

title = customtkinter.CTkLabel(app, text="INSERT A YOUTUBE LINK", font=("Segoe UI Black",20, "normal"))
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, font=("Segoe UI", 15, "bold"))
link.pack()

finished_label = customtkinter.CTkLabel(app, text=" ", font=("Segoe UI", 15, "bold") )
finished_label.pack()

pPercentage = customtkinter.CTkLabel(app, text="0%", font=("Segoe UI", 15, "bold") )
pPercentage.pack()

pProgressbar = customtkinter.CTkProgressBar(app, width=400)
pProgressbar.set(0)
pProgressbar.pack(pady=10)

downlaod = customtkinter.CTkButton(app, text="Download", command=verify, font=("Segoe UI Black",20, "normal"))
downlaod.pack(pady=10)
#Run App
app.mainloop()
#Made by mg
#github: