from PIL import Image as img
import time
from tkinter import *
from tkinter import ttk
from urllib.request import urlopen
from io import BytesIO

imgURL = 'https://i.scdn.co/image/ab67616d0000b2734e5df11b17b2727da2b718d8'

URL = imgURL
u = urlopen(URL)
raw_data = u.read()
u.close()

im = img.open(BytesIO(raw_data))

im1 = im.convert('RGBA')

black_im = img.open('kwlos.png')

print('album: ', im1.mode)
print('black: ', black_im.mode)