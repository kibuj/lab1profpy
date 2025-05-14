from tkinter import *
from tkinter import colorchooser, simpledialog


settings = {
    'triangle': {'color': 'yellow', 'size': 1.0},
    'rectangle': {'color': 'blue', 'size': 1.0},
    'circle': {'color': 'green', 'size': 1.0},
    'text': {'triangle': {'size': 14, 'color': 'blue'},
             'rectangle': {'size': 14, 'color': 'black'},
             'circle': {'size': 14, 'color': 'green'}}
}


def update_text(shape_name, message):
    text.delete(1.0, END)
    text.insert(1.0, message)
    size = settings['text'][shape_name]['size']
    color = settings['text'][shape_name]['color']
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', size), foreground=color)


def triangle():
    canvas.coords(r, (0, 0, 0, 0))
    canvas.coords(c, (0, 0, 0, 0))
    color = settings['triangle']['color']
    scale = settings['triangle']['size']
    canvas.itemconfig(t, fill=color, outline='white')
    points = [50, 200, 340, 200, 110, 60]
    scaled = [coord * scale for coord in points]
    canvas.coords(t, *scaled)
    update_text('triangle', 'Зображення трикутника')

def rectangle():
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(c, (0, 0, 0, 0))
    color = settings['rectangle']['color']
    scale = settings['rectangle']['size']
    canvas.itemconfig(r, fill=color, outline='white')
    coords = [80, 50, 320, 200]
    scaled = [coord * scale for coord in coords]
    canvas.coords(r, *scaled)
    update_text('rectangle', 'Зображення прямокутника')

def circle():
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(r, (0, 0, 0, 0))
    color = settings['circle']['color']
    scale = settings['circle']['size']
    canvas.itemconfig(c, fill=color, outline='white')
    coords = [100, 60, 300, 260]
    scaled = [coord * scale for coord in coords]
    canvas.coords(c, *scaled)
    update_text('circle', 'Зображення кола')

def clear_canvas():
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(r, (0, 0, 0, 0))
    canvas.coords(c, (0, 0, 0, 0))
    text.delete(1.0, END)


def configure_images():
    for shape in ['triangle', 'rectangle', 'circle']:
        color = colorchooser.askcolor(title=f"Оберіть колір для {shape}")[1]
        if color:
            settings[shape]['color'] = color
        size = simpledialog.askfloat("Розмір фігури", f"Введіть масштаб (0.1 - 3.0) для {shape}", minvalue=0.1, maxvalue=3.0)
        if size:
            settings[shape]['size'] = size


def configure_text():
    for shape in ['triangle', 'rectangle', 'circle']:
        color = colorchooser.askcolor(title=f"Оберіть колір тексту для {shape}")[1]
        if color:
            settings['text'][shape]['color'] = color
        size = simpledialog.askinteger("Розмір тексту", f"Введіть розмір шрифту для {shape}", minvalue=8, maxvalue=48)
        if size:
            settings['text'][shape]['size'] = size


win = Tk()
win.title("Фігури з налаштуваннями")


menu = Menu(win)
win.config(menu=menu)
settings_menu = Menu(menu, tearoff=0)
settings_menu.add_command(label="Налаштування зображень", command=configure_images)
settings_menu.add_command(label="Налаштування тексту", command=configure_text)
menu.add_cascade(label="Налаштування", menu=settings_menu)


b_triangle = Button(text="Трикутник", width=15, command=triangle)
b_rectangle = Button(text="Прямокутник", width=15, command=rectangle)
b_circle = Button(text="Коло", width=15, command=circle)
b_clear = Button(text="Очистити", width=15, command=clear_canvas)


canvas = Canvas(width=400, height=300, bg='#fff')
text = Text(width=55, height=5, bg='#fff', wrap=WORD)


t = canvas.create_polygon(0, 0, 0, 0, 0, 0)
r = canvas.create_rectangle(0, 0, 0, 0)
c = canvas.create_oval(0, 0, 0, 0)


b_triangle.grid(row=0, column=0)
b_rectangle.grid(row=1, column=0)
b_circle.grid(row=2, column=0)
b_clear.grid(row=3, column=0)
canvas.grid(row=0, column=1, rowspan=10)
text.grid(row=11, column=1, rowspan=3)

win.mainloop()
