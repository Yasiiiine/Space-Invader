from tkinter import *

class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 50, 50, fill="green")
        self.canvas.move(self.id, 275, 350)
        self.lives = 3

    def move_left(self, event):
        self.canvas.move(self.id, -20, 0)

    def move_right(self, event):
        self.canvas.move(self.id, 20, 0)

    def shoot(self):
        x, y, _, _ = self.canvas.coords(self.id)
        return self.canvas.create_rectangle(x + 20, y, x + 30, y - 10, fill="yellow")

    def update(self):
        pass
