from tkinter import *
from pytube import YouTube
from tkinter import *
from PIL import ImageTk,Image
root=Tk()

def download():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download()
    Label(root, text= "Downloaded Successfully")


root.geometry('500x500')
root.resizable(0,0)
root.title(" My video downloader")
root.config(background="black")
#adding icon
root.iconbitmap("C:/Users/HP/Downloads/Youtube_icon-icons.com_66802.ico")

#adding logo
logo1=Image.open("C:/Users/HP/Downloads/YOUTUBE_icon-icons.com_65487.png")
resize1=logo1.resize((70, 70))
logo_insertion=ImageTk.PhotoImage(resize1)
Label(root, image=logo_insertion).pack()



link=StringVar()


#gets the text to paste your link
Label(root, text="Paste your link here" ,font="arial 10 italic" ,pady=-20, padx=5).place(x=20, y=65)



#for making space to write or paste the link
link_enter= Entry(root, width=90 , textvariable=link).place(x=20 , y=90)

#for making the download button
Button(root, text="Download" , font ="arial 20 bold" , command=download ). place(x=160 , y=300)

root.mainloop()