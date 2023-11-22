import tkinter as tk
import random
import time

window = tk.Tk()
window.title('name the colour')
window.geometry('450x250')

colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple', 'black', 'white', 'brown', 'pink', 'grey']
score = 0
fails = 0
time_left = 8

time_label = tk.Label(window, text=f'seconds left:{time_left}')
time_label.place(x=10, y=210)

score_label = tk.Label(window, text=f'right:{score}', font=('Helvetica', 10))
score_label.place(x=10, y=40)

fails_label = tk.Label(window, text=f'wrong:{fails}', font=('Helvetica', 10))
fails_label.place(x=10, y=60)

def timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label['text'] = f'seconds left:{time_left}'
        time_label.after(1000, timer)

def new_word():
    color_label['text'] = random.choice(colors)
    color_label['fg'] = random.choice(colors)

def check(event):
    global score
    global fails
    global time_left
    if time_left > 0:
        user_color = entry.get()
        word_color = color_label['fg']
        if user_color == word_color:
            print('yes')
            score += 1
            print(score)
            score_label['text'] = f'right:{score}'
        else:
            print('no')
            fails += 1
            print(fails)
            fails_label['text'] = f'wrong:{fails}'
        new_word()
        entry.delete(0, 'end')
        time_left = 8
        time_label['text'] = f'seconds left:{time_left}'

instructions = tk.Label(window, width=50, text='Enter the colour of the word but not the word itself. Press enter to play!', font=('Helvetica', 10))
instructions.place(x=10, y=10)

color_label = tk.Label(window, text='colour', font=('Helvetica', 60))
color_label.place(x=10, y=80)

entry = tk.Entry(window, font=('Helvetica', 10),)
entry.place(x=10, y=180)

entry.focus_set()

new_word()
window.bind('<Return>', check)
timer()
window.mainloop()

'''В функции timer: после блока условия if time_left > 0 добавить блок else, в котором выводить всплывающее окно из библиотеки tkinter.messagebox - "Конец игры", "Время вышло". 
В функции check: после блока условия if time_left > 0 добавить блок else, в котором делаем проверку - если правильных ответов больше неправильных - сделать всплывающее окно - "Хороший результат", "Ты молодец". Иначе - "Неважный результат", "В следующий раз получится лучше".
'''
