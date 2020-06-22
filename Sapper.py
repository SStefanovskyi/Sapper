from tkinter import *
import random

grid_size = 8       #Ширина і висота поля
square_size = 50    #Розмір клітинки на полі
mines_num = 10      #Кількість мін на полі
mines = set(random.sample(range(1, grid_size**2+1), mines_num))     #Генеруємо міни в випадковому порядку
clicked = set()     #Створюєму сет для клітинок, по яким ми клікнули

#Функція реагування на клік
def click(event):
    ids = c.find_withtag(CURRENT)[0]    #Оприділяємо по якій клітинці клікнули
    if ids in mines:
        c.itemconfig(CURRENT, fill = "red")     #Якщо клікнули по клітинці з міною, то красимо її в червоний колір
    elif ids not in clicked:
        c.itemconfig(CURRENT, fill = "green")   #Інакше красимо в зелений
    c.update()

#Функція для обозначення мін
def mark_mine(event):
    ids = c.find_withtag(CURRENT)[0]
    #Якщо ми не клікали по клітинці - фарбуємо її в жовтий колір
    if ids not in clicked:
        clicked.add(ids)
        x1, y1, x2, y2 = c.coords(ids)
        c.itemconfig(CURRENT, fill = "yellow")
    else:
        clicked.remove(ids)
        c.itemconfig(CURRENT, fill = "grey")

root = Tk()         #Основне вікно програми
root.title("Pythonicway Minesweep")
c = Canvas(root, width = grid_size * square_size, height = grid_size * square_size)     #Задаємо область на якій будемо малювати

c.pack()
c.bind("<Button-1>", click)
c.bind("<Button-3>", mark_mine)

#Малюємо ришітку із клітинок сірого кольору на ігровому полі
for i in range(grid_size):
    for j in range(grid_size):
        c.create_rectangle(i * square_size, j * square_size,
                           i * square_size + square_size,
                           j * square_size + square_size, fill = 'gray')

root.mainloop()     #Запускаємо програму
