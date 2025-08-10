#from cProfile import labelbhi
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



#Calling the octave function that loads in the database needed to match the recording to a song
def load():
    #Adding path to octave directory
    octave.addpath(octave.genpath('../octave-dir/'))
    #Calling the function
    octave.eval('main')

#Calling it
load()

#Call the octave function that handles the recording of the song in question
def recordena():
    #Making changes to the GUI
    loading_label = Label(root, bg='#008bff', image = listening, bd=0)
    loading_label.image = listening
    loading_label.place(relx=0.5, rely=0.75, anchor=CENTER)
    #GOTO line 18, 20
    octave.addpath('../octave-dir/')
    r = octave.recordena()

    results(r)

#Animating the button on click 
def REC_clicked():
    global pos, count1
    if count1 < 100:
        pos -= 1
        count1 += 1
        recordButton.pack_configure(pady=pos)
        root.after(1, REC_clicked)

#Play the song when the right button is pressed
def play_song(r):
    url = r
    webbrowser.open(url,new=1)
   
#Variables used by the functions handling the animations
count=0
count1=0
size=300
pos=100

#This and the expand function handle the "breathing" animation of the button
#The one calls the other in an infinite loop setup so the animation doesn't stop
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

#This function handles displaying the result on the GUI
#Also handles necessary changes to the GUI to move from the starting screen to the results screen
def results(r):
    octave.addpath('../octave-dir/')
    #resN: songs name, resAN: artists name, imgURL: url to display the image on the result screen, resPURL: url to play the song on the web if requested
    resN, resAN, imgURL, resPURL = octave.results(r,nout=4)
    
    #recordButton.destroy()

    #To line 103: Code to display the image on the results screen
    URL = imgURL
    u = urlopen(URL)
    raw_data = u.read()
    u.close()

    im = img.open(BytesIO(raw_data))
    photo = ImageTk.PhotoImage(im)
    label = ttk.Label(image=photo)
    label.image = photo
    label.place(relx=0.5, rely=0.4, anchor=CENTER)

    #Label to display the songs and artists name
    resultsLabel = ttk.Label(root, text=f"Your song is: {resN}, by: {resAN}!",font=('Raleway', 12))
    resultsLabel.place(relx=0.5, rely=0.895, anchor=CENTER)
    resultsLabel.config(background='#3b3c44',borderwidth=0,foreground='white',)

    #Image for button to play the song on the web if requested
    play_im = img.open('play.png')
    play_im_prov = play_im.resize((56,56))
    play_photo = ImageTk.PhotoImage(play_im_prov)

    #Button to play the song on the web if requested
    play_button = Button(root, image=play_photo, command = lambda: play_song(resPURL),bg='#3b3c44',borderwidth=0,highlightthickness=0,activebackground='#3b3c44')
    play_button.image=play_photo
    play_button.place(relx=0.5, rely=0.95, anchor=CENTER)

    #Image for the "return to starting screen" button
    back_im = img.open('return.png') #/backbtn.png
    back_im_prov = back_im.resize((56,56))
    back_photo = ImageTk.PhotoImage(back_im_prov)

    #Return to starting screen button
    back_button = Button(root, image=back_photo, command=lambda: back_to_homescreen(),bg='#3b3c44',borderwidth=0,highlightthickness=0,activebackground='#3b3c44')
    back_button.image=back_photo
    back_button.place(relx=0.9,rely=0.95, anchor=CENTER)

    #Changing background color
    root.config(bg='#3b3c44',borderwidth=0,highlightthickness=0)
    
    #Function that the "return to starting screen" button calls
    def back_to_homescreen():
        #To line 138: Resetting some values, so that the on-click animation can play again for the second recording
        global pos, count1
        pos = 100
        count1 = 0
        #To line 160: GUI changes
        label.destroy()
        resultsLabel.destroy()
        play_button.destroy()
        back_button.destroy()

        root.config(bg='#008bff')

        photo = img.open("khazam-ico.png")
        resized = photo.resize((300,300), img.Resampling.LANCZOS)
        newphoto = ImageTk.PhotoImage(resized)

        text = img.open("text-logo.png")
        resized_text = text.resize((432,73), img.Resampling.LANCZOS)
        newtext = ImageTk.PhotoImage(resized_text)

        recordButton.place(relx=0.5, rely=0.5, anchor=CENTER)

        khazam_label = Label(root, bg='#008bff', image=newtext, bd=0)
        khazam_label.image = newtext
        khazam_label.place(relx=0.5, rely=0.75, anchor=CENTER)



#To line 191: The starting screen GUI
root = Tk()
kh_img = PhotoImage(file='khazam-ico.png')
root.tk.call('wm', 'iconphoto', root._w, kh_img)
root.title('Khazam')
root.geometry('640x720')
root.resizable(0, 0)
root.config(bg='#008bff')


photo = img.open("khazam-ico.png")
resized = photo.resize((300,300), img.Resampling.LANCZOS)
newphoto = ImageTk.PhotoImage(resized)

text = img.open("text-logo.png")
resized_text = text.resize((432,73), img.Resampling.LANCZOS)
newtext = ImageTk.PhotoImage(resized_text)

listening = img.open("listening-logo.png")
resized_listening = listening.resize((432,73), img.Resampling.LANCZOS)
listening = ImageTk.PhotoImage(resized_listening)


recordButton = Button(root, bg='#008bff', activebackground='#008bff', command= lambda: [threading.Thread(target=recordena).start(),REC_clicked()], highlightthickness=0, bd=0)
recordButton.place(relx=0.5, rely=0.5, anchor=CENTER)

khazam_label = Label(root, bg='#008bff', image=newtext, bd=0)
khazam_label.image = newtext
khazam_label.place(relx=0.5, rely=0.75, anchor=CENTER)

#Calling the function that begins the "breathing" animation
expand()

root.mainloop()
