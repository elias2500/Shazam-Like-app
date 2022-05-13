#from cProfile import label
from tkinter import *
from tkinter import ttk
from oct2py import octave
from PIL import Image as img
from PIL import ImageTk
from urllib.request import urlopen
from io import BytesIO
import webbrowser
import threading
from time import sleep
#from pygments import highlight



def hide_button(b):
    b.pack_forget()

def load():
    octave.addpath(octave.genpath('/home/ilias/Downloads/fingerprint_prototype-20220414T171621Z-001/fingerprint_prototype'))
    octave.run('main')

load()

def recordena():
    #khazam_label.destroy()
    loading_label = Label(root, bg='#008bff', image = listening, bd=0)
    loading_label.image = listening
    loading_label.place(relx=0.5, rely=0.75, anchor=CENTER)
    octave.addpath('/home/ilias/Downloads/fingerprint_prototype-20220414T171621Z-001/fingerprint_prototype')
    r = octave.recordena()

    #loading_label.destroy()
    results(r)
    
def REC_clicked():
    global pos, count1
    if count1 < 100:
        pos -= 1
        count1 += 1
        recordButton.pack_configure(pady=pos)
        root.after(1, REC_clicked)


def play_song(r):
    url = r
    webbrowser.open(url,new=1)
   
count=0
count1=0
size=300
pos=100

def contract():
    global count, size
    if count <= 10 and count > 0:
       size -= 3
       count -= 1
       tmp_images = ImageTk.PhotoImage(photo.resize((size, size))) # the image size
       recordButton.image = tmp_images # keep reference
       recordButton["image"] = tmp_images # change the image
       root.after(20, contract)
    elif count == 0:
       expand()

def expand():
    global count, size
    if count < 10:
       size += 3
       count += 1
       tmp_images = ImageTk.PhotoImage(photo.resize((size, size))) # the image size
       recordButton.image = tmp_images # keep reference
       recordButton["image"] = tmp_images # change the image
       root.after(20, expand) 
    elif count == 10:
       contract()

def results(r):
    octave.addpath('/home/ilias/Downloads/fingerprint_prototype-20220414T171621Z-001/fingerprint_prototype')
    resN, resAN, imgURL, resPURL = octave.results(r,nout=4)
    
    #recordButton.destroy()

    URL = imgURL
    u = urlopen(URL)
    raw_data = u.read()
    u.close()

    im = img.open(BytesIO(raw_data))
    photo = ImageTk.PhotoImage(im)
    label = ttk.Label(image=photo)
    label.image = photo
    label.place(relx=0.5, rely=0.4, anchor=CENTER)

    resultsLabel = ttk.Label(root, text=f"Your song is: {resN}, by: {resAN}!",font=('Raleway', 12))
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

    root.config(bg='#3b3c44',borderwidth=0,highlightthickness=0)
    
    def back_to_homescreen():
        global pos, count1
        pos = 100
        count1 = 0
        label.destroy()
        resultsLabel.destroy()
        play_button.destroy()
        back_button.destroy()

        root.config(bg='#008bff')

        photo = img.open("khazam-ico.png")
        resized = photo.resize((300,300), img.ANTIALIAS)
        newphoto = ImageTk.PhotoImage(resized)

        text = img.open("text-logo.png")
        resized_text = text.resize((432,73), img.ANTIALIAS)
        newtext = ImageTk.PhotoImage(resized_text)

        #recordButton = Button(root, bg='#008bff', activebackground='#008bff', command= lambda: [threading.Thread(target=recordena).start(),REC_clicked()], highlightthickness=0, bd=0)
        recordButton.place(relx=0.5, rely=0.5, anchor=CENTER)

        khazam_label = Label(root, bg='#008bff', image=newtext, bd=0)
        khazam_label.image = newtext
        khazam_label.place(relx=0.5, rely=0.75, anchor=CENTER)




root = Tk()
kh_img = PhotoImage(file='khazam-ico.png')
root.tk.call('wm', 'iconphoto', root._w, kh_img)
root.geometry('640x720')
root.resizable(0, 0)
root.config(bg='#008bff')


photo = img.open("khazam-ico.png")
resized = photo.resize((300,300), img.ANTIALIAS)
newphoto = ImageTk.PhotoImage(resized)

text = img.open("text-logo.png")
resized_text = text.resize((432,73), img.ANTIALIAS)
newtext = ImageTk.PhotoImage(resized_text)

listening = img.open("listening-logo.png")
resized_listening = listening.resize((432,73), img.ANTIALIAS)
listening = ImageTk.PhotoImage(resized_listening)


recordButton = Button(root, bg='#008bff', activebackground='#008bff', command= lambda: [threading.Thread(target=recordena).start(),REC_clicked()], highlightthickness=0, bd=0)
recordButton.place(relx=0.5, rely=0.5, anchor=CENTER)

khazam_label = Label(root, bg='#008bff', image=newtext, bd=0)
khazam_label.image = newtext
khazam_label.place(relx=0.5, rely=0.75, anchor=CENTER)

expand()

root.mainloop()