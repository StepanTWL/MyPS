import tkinter as tk

window = tk.Tk()
icon = tk.PhotoImage(file='Image\icon.png')
window.iconphoto(False, icon)
window.config(bg='white')  # белый фон
window.title('My Photoshop')
window.geometry('500x600+800+100')
window.resizable(False, False)  # блокировка изменения размера окна

btn_open = tk.Button(window, text='Open')
btn_turn_left = tk.Button(window)
btn_turn_right = tk.Button(window)
btn_mirror_hor = tk.Button(window)
btn_mirror_vert = tk.Button(window)
image = tk.Image(file='Image\icon.png')

btn_open.grid(row=0, column=0, sticky='w')
#btn2.grid(row=0, column=1, sticky='e')
#btn3.grid(row=1, column=0, columnspan=2, sticky='we')
#btn4.grid(row=0, column=2, rowspan=2, sticky='ns')
window.grid_columnconfigure(0, minsize=70)

for i in range(2, 7):
    for j in range(3, 5):
        tk.Button(window, text=f"Hello {i} {j}").grid(row=i, column=j)

window.mainloop()
