from tkinter import *
import random
root = Tk()
def random_game():
    list_game = ['Pong', 'Flappy bird', 'Snake', 'Goose', 'Monsters', '3D game']
    rand_game = random.choice(list_game)
    l['text'] = f'{rand_game}'
root.title('Random game')
root.geometry('600x600')
root.config(bg = 'Black')
root.resizable(width = False, height = False)
l = Label(root, text = '...',
          font = 'arial, 30',
          bg = 'Black',
          fg = 'Blue')
l.pack()
b = Button(root, text = 'Random',
           command = random_game,
           width = 30,
           bg = 'Grey',
           fg = 'White')
b.pack()
root.mainloop()
