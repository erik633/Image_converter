# from PIL import Image
import PIL.Image
import os
import re
from tkinter import *
from tkinter import filedialog
# import sys

def show_picture():
    try:
        import_file_path = filedialog.askopenfilename()
        im1 = PIL.Image.open(import_file_path)
        im1.show()
    except:
        pass

def convert_jpg_to_png():
    try:
        import_file_path = filedialog.askopenfilename()
        for match in re.finditer(r'(\w*.\w{3}$)', import_file_path):
            file = match.group(0)
            path = import_file_path.split(file)[0]
            clean_name = os.path.splitext(file)[0]
            im1 = PIL.Image.open(import_file_path)
            im1.save(f'{path}{clean_name}.png', 'png')
            im1.show()
    except:
        pass

def convert_png_to_jpg():
    try:
        import_file_path = filedialog.askopenfilename()
        for match in re.finditer(r'(\w*.\w{3}$)', import_file_path):
            file = match.group(0)
            path = import_file_path.split(file)[0]
            clean_name = os.path.splitext(file)[0]
            im1 = PIL.Image.open(import_file_path)
            im1.save(f'{path}{clean_name}.jpeg', 'jpeg')
            im1.show()
    except:
        pass

root = Tk()
root.title("Convert image files")
root.geometry("500x500+500+200")

label = Label(root, text="WELCOME TO 'IMAGE CONVERTER'", font=(None, 30), height=10, width=10, bg="lightblue")
label.pack(fill=BOTH, expand=TRUE)
b1 = Button(root, text="SHOW PICTURE", command=show_picture)
b1.pack(fill=BOTH, expand=TRUE)
b2 = Button(root, text="CONVERT JPG/JPEG TO PNG", command=convert_jpg_to_png)
b2.pack(fill=BOTH, expand=TRUE)
b3 = Button(root, text="CONVERT PNG TO JPEG", command=convert_png_to_jpg)
b3.pack(fill=BOTH, expand=TRUE)

mainloop()


