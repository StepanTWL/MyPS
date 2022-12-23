import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd


#text_editor = tk.Text()


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
            image_file = Image.open(filepath)
            image_file = image_file.resize((300, 300), Image.Resampling.LANCZOS)
        our_image = ImageTk.PhotoImage(image_file)
        #our_lable = tk.Label(window)
        our_lable.image = our_image
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


def create_horizontal_image(image_path):
    image_pixels_list = []
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    # Добавляем вертикальные линии в обратном порядке
    for w in range(width):
        vertical_line = []
        for h in range(height):
            vertical_line.append(pixels[w, h])
        image_pixels_list.insert(0, vertical_line)

    # Записываем готовые пиксели
    for w in range(width):
        for h in range(height):
            pixels[w, h] = image_pixels_list[w][h]
    # img.save(f"{int(time.time())}.jpeg")


def create_vertical_image(image_path):
    image_pixels_list = []
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    # Добавляем вертикальные линии в обратном порядке
    for h in range(height):  # may be width-1
        horizontal_line = []
        for w in range(width):  # may be height-1
            horizontal_line.append(pixels[w, h])
        image_pixels_list.insert(0, horizontal_line)

    # Записываем готовые пиксели
    for w in range(width):
        for h in range(height):
            pixels[w, h] = image_pixels_list[w][h]
    # img.save(f"{int(time.time())}.jpeg")


def create_left_image(image_path):
    image_pixels_list = []
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    for h in range(height):  # may be width-1
        horizontal_line = []
        for w in range(width):  # may be height-1
            horizontal_line.append(pixels[w, h])
        image_pixels_list.insert(horizontal_line, h)

    # Записываем готовые пиксели
    for w in range(width):
        for h in range(height):
            pixels[h, w] = image_pixels_list[h][w]
    # img.save(f"{int(time.time())}.jpeg")


def create_right_image(image_path):
    image_pixels_list = []
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    for h in range(height):  # may be width-1
        horizontal_line = []
        for w in range(width):  # may be height-1
            horizontal_line.append(pixels[w, h])
        image_pixels_list.insert(horizontal_line, height - h - 1)

    # Записываем готовые пиксели
    for w in range(width):
        for h in range(height):
            pixels[h, w] = image_pixels_list[h][w]
    # img.save(f"{int(time.time())}.jpeg")


window = tk.Tk()
window.iconphoto(False, tk.PhotoImage(file=r'Image\icon.png'))
window.config(bg='white')  # белый фон
window.title('My Photoshop')
window.geometry('500x600+800+100')
window.resizable(False, False)  # блокировка изменения размера окна

image_left = Image.open(r'Image\turn-left-button.png')
image_left = image_left.resize((20, 20), Image.Resampling.LANCZOS)
image_left = ImageTk.PhotoImage(image_left)
btn_turn_left = tk.Button(window, image=image_left)
image_right = Image.open(r'Image\turn-right-button.png')
image_right = image_right.resize((20, 20), Image.Resampling.LANCZOS)
image_right = ImageTk.PhotoImage(image_right)
btn_turn_right = tk.Button(window, image=image_right)
image_horiz = Image.open(r'Image\mirror-horizontal-button.png')
image_horiz = image_horiz.resize((20, 20), Image.Resampling.LANCZOS)
image_horiz = ImageTk.PhotoImage(image_horiz)
btn_mirror_hor = tk.Button(window, image=image_horiz)
image_vertic = Image.open(r'Image\mirror-vertical-button.png')
image_vertic = image_vertic.resize((20, 20), Image.Resampling.LANCZOS)
image_vertic = ImageTk.PhotoImage(image_vertic)
btn_mirror_vert = tk.Button(window, image=image_vertic, command=create_vertical_image)



btn_open = tk.Button(window, text='Open', command=open_file)
btn_save = tk.Button(window, text='Save', command=save_file)



our_image = ImageTk.PhotoImage(file=r'Image\no-image.png')
our_lable = tk.Label(window)
our_lable.image = our_image
our_lable['image'] = our_lable.image
our_lable.place(x=100, y=50)


btn_open.place(x=370, y=550, width=100, height=30)
btn_save.place(x=260, y=550, width=100, height=30)
btn_turn_left.place(x=30, y=550, width=30, height=30)
btn_turn_right.place(x=70, y=550, width=30, height=30)
btn_mirror_hor.place(x=110, y=550, width=30, height=30)
btn_mirror_vert.place(x=150, y=550, width=30, height=30)
window.grid_columnconfigure(0, minsize=70)

window.mainloop()
