from cProfile import label
from tkinter import *
from tkinter import ttk
from oct2py import octave
from PIL import Image as img
from PIL import ImageTk
from urllib.request import urlopen
from io import BytesIO
import webbrowser

from pygments import highlight

def hide_button(b):
    b.pack_forget()

def load():
    octave.addpath(octave.genpath('/home/ilias/Downloads/fingerprint_prototype-20220414T171621Z-001/fingerprint_prototype'))
    octave.run('main')

load()

def recordena():
    octave.addpath('/home/ilias/Downloads/fingerprint_prototype-20220414T171621Z-001/fingerprint_prototype')
    r = octave.recordena()

    results(r)

def play_song(r):
    url = r
    webbrowser.open(url,new=1)
   

def results(r):
    octave.addpath('/home/ilias/Downloads/fingerprint_prototype-20220414T171621Z-001/fingerprint_prototype')
    resN, resAN, imgURL, resPURL = octave.results(r,nout=4)
    
    recordButton.destroy()

    root.config(bg='#3b3c44',borderwidth=0,highlightthickness=0)

    URL = imgURL
    u = urlopen(URL)
    raw_data = u.read()
    u.close()

    im = img.open(BytesIO(raw_data))
    photo = ImageTk.PhotoImage(im)
    label = ttk.Label(image=photo)
    label.image = photo
    label.place(relx=0.5, rely=0.4, anchor=CENTER)

    resultsLabel = ttk.Label(root, text=f"Your song is: {resN}, by: {resAN}!",font=('JosefinSans', 12))
    resultsLabel.place(relx=0.5, rely=0.9, anchor=CENTER)
    resultsLabel.config(background='#3b3c44',borderwidth=0,foreground='white',)


    play_im = img.open('/home/ilias/Desktop/karudis/playbtn.png')
    play_im_prov = play_im.resize((40,40))
    play_photo = ImageTk.PhotoImage(play_im_prov)

    play_button = Button(root, image=play_photo, command = lambda: play_song(resPURL),bg='#3b3c44',borderwidth=0,highlightthickness=0,activebackground='#3b3c44')
    play_button.image=play_photo
    play_button.place(relx=0.5, rely=0.95, anchor=CENTER)

    back_im = img.open('/home/ilias/Desktop/karudis/backbtn.png')
    back_im_prov = back_im.resize((40,40))
    back_photo = ImageTk.PhotoImage(back_im_prov)

    back_button = Button(root, image=back_photo, command=lambda: back_to_homescreen(),bg='#3b3c44',borderwidth=0,highlightthickness=0,activebackground='#3b3c44')
    back_button.image=back_photo
    back_button.place(relx=0.9,rely=0.95, anchor=CENTER)
    
    def back_to_homescreen():
        label.destroy()
        resultsLabel.destroy()
        play_button.destroy()
        back_button.destroy()
        recordButton = ttk.Button(root, text='Record', command=recordena)
        recordButton.place(relx=0.5, rely=0.5, anchor=CENTER)
        root.config(bg='blue')


root = Tk()
root.geometry('640x720')
root.resizable(0, 0)
#root.config(bg='blue')

recordButton = ttk.Button(root, text='Record', command=recordena)
recordButton.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()