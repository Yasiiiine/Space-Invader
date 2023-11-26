from tkinter import *
import random

class Enemy:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 30, 30, fill="red")
        self.x = x
        self.y = y
        self.speed = 2
        self.direction = 1
        self.shoot_chance = 0.02  # Probability of shooting

    def move(self):
        self.x += self.speed * self.direction
        self.canvas.coords(self.id, self.x, self.y, self.x + 30, self.y + 30)
        if self.x + 30 >= 550 or self.x <= 0:
            self.direction *= -1

    def shoot(self):
        if random.random() < self.shoot_chance:
            x, y, _, _ = self.canvas.coords(self.id)
            return self.canvas.create_rectangle(x + 15, y + 30, x + 20, y + 40, fill="purple")
        return None

