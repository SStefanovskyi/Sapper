#!/usr/bin/env python

from tkinter import *
import random

grid_size = 20       #Ширина і висота поля
square_size = 20    #Розмір клітинки на полі
mines_num = 40      #Кількість мін на полі
mines = set(random.sample(range(1, grid_size**2+1), mines_num))     #Генеруємо міни в випадковому порядку
clicked = set()     #Створюєму сет для клітинок, по яким ми клікнули

def check_mines(neighbors):
    return len(mines.intersection(neighbors))

def generate_neighbors(square):
    #Повертаємо клітинки які сусідні з square
    #Ліва верхня клітинка
    if square == 1:
        data = {grid_size + 1, 2, grid_size + 2}
    #права нижня
    elif square == grid_size ** 2:
        data = {square - grid_size, square - 1, square - grid_size - 1}
    #Ліва нижня
    elif square == grid_size:
        data = {grid_size - 1, grid_size * 2, grid_size * 2 - 1}
    #Верхня права
    elif square == grid_size ** 2 - grid_size +1:
        data = {square + 1, square - grid_size, square - grid_size + 1}
    #Клітинка в лівому ряду
    elif square < grid_size:
        data = {square + 1, square - 1, square + grid_size, square + grid_size - 1, square + grid_size + 1}
    #Клітинка в правому ряду
    elif square > grid_size ** 2 - grid_size:
        data = {square + 1, square - 1, square - grid_size, square - grid_size - 1, square - grid_size + 1}
    #Клітинка в нижньому ряду
    elif square % grid_size == 0:
        data = {square + grid_size, square - grid_size, square - 1, square + grid_size - 1, square - grid_size - 1}
    #Клітинка в верхньому рядку
    elif square % grid_size == 1:
        data = {square + grid_size, square - grid_size, square + 1, square + grid_size + 1, square - grid_size + 1}
    #Люба інша клітинка
    else:
        data = {square - 1, square + 1, square - grid_size, square + grid_size, square - grid_size - 1, square - grid_size +1, square + grid_size + 1, square + grid_size - 1}
    return data

def clearance(ids):
    #Інтерактивна функція очистки поля
    clicked.add(ids)    #Додаємо натиснуту клітинку в сет натиснутих
    ids_neigh = generate_neighbors(ids)     #Отримуємо всі сусідні клітинки
    around = check_mines(ids_neigh)     #Вираховуємо кількість мін навколо натиснутої клітинки
    c.itemconfig(ids, fill = "green")       #Красимо клітинку в зелений

    #Якщо навколо немає мін
    if around == 0:
        #Створюємо список сусідніх клітинок
        neigh_list = list(ids_neigh)
        #Поки в списку сусусідів є клітинки
        while len(neigh_list) > 0:
            #Отримуємо клітинку
            item = neigh_list.pop()
            #Фарбуємо її в зелений колір
            c.itemconfig(item, fill = "green")
            #Отримуємо сусідні клітинки даної клітинки
            item_neigh = generate_neighbors(item)
            #Получаємо кількість мін в сусідніх клітинках
            item_aroind = check_mines(item_neigh)
            #Якщо в сусідніх клітинках є міни
            if item_aroind > 0:
                #Робимо перевірку, щоб не писати декілька раз на одній і тій же клітинці
                if item not in clicked:
                    #Отримуємо координати цієї клітинки
                    x1, y1, x2, y2 = c.coords(item)
                    #Пишимо на клітинці кількість мін навколо
                    c.create_text(x1 + square_size / 2,
                                  y1 + square_size / 2,
                                  text = str(item_aroind),
                                  font = "Arial {}".format(int(square_size / 2)),
                                  fill = 'yellow')
            #Якщо в сусідніх клітинках немає мін
            else:
                #Додаємо сусідні клітинки даної клітинки в общий список
                neigh_list.extend(set(item_neigh).difference(clicked))
                #Убираємо елементи які повторюються з общого списку
                neigh_list = list(set(neigh_list))
            #Додаємо клітинку в натиснуті
            clicked.add(item)
    #Якщо міни навколо є
    else:
        #Вираховуємо координати клітинкі
        x1, y1, x2, y2 = c.coords(ids)
        #Пишемо кількість мін навколо
        c.create_text(x1 + square_size / 2,
                      y1 + square_size / 2,
                      text = str(around),
                      font = "Arial {}".format(int(square_size / 2)),
                      fill = 'yellow')

#Функція реагування на клік
def click(event):
    ids = c.find_withtag(CURRENT)[0]    #Оприділяємо по якій клітинці клікнули
    if ids in mines:
        c.itemconfig(CURRENT, fill = "red")     #Якщо клікнули по клітинці з міною, то красимо її в червоний колір
    elif ids not in clicked:
        clearance(ids)
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
c.bind("<Button-1>", click)
c.bind("<Button-3>", mark_mine)
c.pack()

#Малюємо ришітку із клітинок сірого кольору на ігровому полі
for i in range(grid_size):
    for j in range(grid_size):
        c.create_rectangle(i * square_size, j * square_size,
                           i * square_size + square_size,
                           j * square_size + square_size, fill = 'gray')

root.mainloop()     #Запускаємо програму
