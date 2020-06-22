from tkinter import *
import random

import click as click

grid_size = 8       #Ширина і висота поля
square_size = 50    #Розмір клітинки на полі
mines_num = 10      #Кількість мін на полі

root = Tk()         #Основне вікно програми
root.title("Pythonicway Minesweep")
c = Canvas(root, width = grid_size * square_size, height = grid_size * square_size)     #Задаємо область на якій будемо малювати
c.pack()

#Малюємо ришітку із клітинок сірого кольору на ігровому полі
for i in range(grid_size):
    for j in range(grid_size):
        c.create_rectangle(i * square_size, j * square_size,
                           i * square_size + square_size,
                           j * square_size + square_size, fill = 'gray')

root.mainloop()     #Запускаэмо програму
