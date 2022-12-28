import tkinter as tk
from pathlib import Path

from PIL import Image, ImageTk, ImageOps
from tkinter import filedialog as fd


def open_file():
    filetypes = (
        ('JPG, JPEG', '*.jpg *.jpeg'),
        ('BMP', '*.bmp'),
        ('PNG', '*.png'),
    )

    filepath = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    if filepath != "":
        with open(filepath, "r") as file:
            our_image = Image.open(filepath)
            our_image = our_image.resize((300, 300), Image.Resampling.LANCZOS)
        our_lable.image = ImageTk.PhotoImage(our_image)
        our_lable['image'] = our_lable.image
        our_lable.place(x=100, y=50)


def save_file():
    filepath = fd.asksaveasfilename()
    """
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)
    """


class create_image:

    def __init__(self):
        self.count = 0

    def left(self, image):
        self.count += 1
        #image = image.rotate(angle=90, expand=True)
        image = image.transpose(Image.Transpose.ROTATE_90)
        our_lable.image = ImageTk.PhotoImage(image)
        our_lable['image'] = our_lable.image
        our_lable.place(x=100, y=50)

    def right(self, image):
        self.count -= 1
        image = image.rotate(angle=90 * self.count, expand=True).copy()
        our_lable.image = ImageTk.PhotoImage(image)
        our_lable['image'] = our_lable.image
        our_lable.place(x=100, y=50)

    def horizontal(self, image):
        image = ImageOps.mirror(image)
        our_lable.image = ImageTk.PhotoImage(image)
        our_lable['image'] = our_lable.image
        our_lable.place(x=100, y=50)

    def vertical(self, image):
        image = ImageOps.flip(image).convert()
        our_lable.image = ImageTk.PhotoImage(image)
        our_lable['image'] = our_lable.image
        our_lable.place(x=100, y=50)


create_image = create_image()

window = tk.Tk()
window.iconphoto(False, ImageTk.PhotoImage(file=Path('Image', 'icon.png')))
window.config(bg='white')  # белый фон
window.title('My Photoshop')
window.geometry('500x600+800+100')
window.resizable(False, False)  # блокировка изменения размера окна

our_image = Image.open(Path('Image', 'no-image.png'))
our_lable = tk.Label(window)
our_lable.image = ImageTk.PhotoImage(our_image)
our_lable['image'] = our_lable.image
our_lable.place(x=100, y=50)

image_left = Image.open(Path('Image', 'turn-left-button.png'))
image_left = image_left.resize((20, 20), Image.Resampling.LANCZOS)
image_left = ImageTk.PhotoImage(image_left)
btn_turn_left = tk.Button(window, image=image_left, command=lambda: create_image.left(our_image))
image_right = Image.open(Path('Image', 'turn-right-button.png'))
image_right = image_right.resize((20, 20), Image.Resampling.LANCZOS)
image_right = ImageTk.PhotoImage(image_right)
btn_turn_right = tk.Button(window, image=image_right, command=lambda: create_image.right(our_image))
image_horiz = Image.open(Path('Image', 'mirror-horizontal-button.png'))
image_horiz = image_horiz.resize((20, 20), Image.Resampling.LANCZOS)
image_horiz = ImageTk.PhotoImage(image_horiz)
btn_mirror_hor = tk.Button(window, image=image_horiz, command=lambda: create_image.horizontal(our_image))
image_vertic = Image.open(Path('Image', 'mirror-vertical-button.png'))
image_vertic = image_vertic.resize((20, 20), Image.Resampling.LANCZOS)
image_vertic = ImageTk.PhotoImage(image_vertic)
btn_mirror_vert = tk.Button(window, image=image_vertic, command=lambda: create_image.vertical(our_image))

btn_open = tk.Button(window, text='Open', command=open_file)
btn_save = tk.Button(window, text='Save', command=save_file)

btn_open.place(x=370, y=550, width=100, height=30)
btn_save.place(x=260, y=550, width=100, height=30)
btn_turn_left.place(x=30, y=550, width=30, height=30)
btn_turn_right.place(x=70, y=550, width=30, height=30)
btn_mirror_hor.place(x=110, y=550, width=30, height=30)
btn_mirror_vert.place(x=150, y=550, width=30, height=30)
window.grid_columnconfigure(0, minsize=70)

window.mainloop()
