from tkinter import *
from google_speech import Speech
from tkinter import scrolledtext
from TextReader import TextReader


window = Tk()

window.title("Text Reader")

window.geometry('500x290')

txt = scrolledtext.ScrolledText(window,width=60,height=12)

txt.grid(column=0,row=0)


def func(event):
    clicked()
window.bind('<Return>', func)


def clicked():

    text = txt.get('1.0', 'end-1c')
    speaker = TextReader(text)
    speaker.speak()
    txt.delete(1.0,END)


btn = Button(window, text="Speak it", command=clicked)

btn.config( height = 2, width = 15 )

btn.grid(column=0, row=1)

window.mainloop()