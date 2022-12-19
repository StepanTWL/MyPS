import tkinter as tk
from PIL import Image, ImageTk


# text_editor = tk.Text()


def open_file():
    filepath = tk.filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            image_file = tk.PhotoImage(file=file)


def save_file():
    filepath = tk.filedialog.asksaveasfilename()
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

image = Image.open(r'Image\turn-left-button.png')
image = image.resize((20,20), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
btn_turn_left = tk.Button(window, image=image)
# image = ImageTk.PhotoImage(file=r'Image\turn-right-button.png-button.png')
# btn_turn_right = tk.Button(window, image=image)
btn_mirror_hor = tk.Button(window, text='Hor')
btn_mirror_vert = tk.Button(window, text='Vert')

btn_open = tk.Button(window, text='Open', command=open_file)
btn_save = tk.Button(window, text='Save', command=save_file)

"""
our_image = tk.PhotoImage(file="Image\_no-image.png")
our_lable = tk.Label(window)
our_lable.image = our_image
our_lable['image'] = our_lable.image
our_lable.place(x=100, y=50)
"""

btn_open.place(x=370, y=550, width=100, height=30)
btn_save.place(x=260, y=550, width=100, height=30)
btn_turn_left.place(x=30, y=550, width=30, height=30)
# btn_turn_right.place(x=70, y=550, width=30, height=30)
btn_mirror_hor.place(x=110, y=550, width=30, height=30)
btn_mirror_vert.place(x=150, y=550, width=30, height=30)
window.grid_columnconfigure(0, minsize=70)

window.mainloop()
