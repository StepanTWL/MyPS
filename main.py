import tkinter as tk
from tkinter import filedialog


def get_file_name():
    file = filedialog.askopenfilename()

window = tk.Tk()
icon = tk.PhotoImage(file='Image\icon.png')
window.iconphoto(False, icon)
window.config(bg='white')  # белый фон
window.title('My Photoshop')
window.geometry('500x600+800+100')
window.resizable(False, False)  # блокировка изменения размера окна

#btn_open = tk.Button(window, text='Open')
btn_save = tk.Button(window, text='Save')
btn_turn_left = tk.Button(window, text='Left')
btn_turn_right = tk.Button(window, text='Right')
btn_mirror_hor = tk.Button(window, text='Hor')
btn_mirror_vert = tk.Button(window, text='Vert')

btn_open = tk.Button(window, text='Open', command=get_file_name)

our_image = tk.PhotoImage(file="Image\_no-image.png")
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
