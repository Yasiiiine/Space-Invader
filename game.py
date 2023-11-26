from tkinter import *
from player import Player
from enemy import Enemy

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Space Invaders")
        self.master.geometry("650x450")

        self.canvas = Canvas(self.master, bg="black", height=400, width=550)
        self.canvas.pack(side='bottom', anchor='nw')

        self.player = Player(self.canvas)
        self.enemies = [Enemy(self.canvas, x, 50) for x in range(50, 500, 60)]
        self.projectiles = []

        self.score_text = self.canvas.create_text(50, 15, text="Score: 0", fill="white")
        self.lives_text = self.canvas.create_text(500, 15, text="Lives: 3", fill="white")

        self.master.bind("<Left>", self.player.move_left)
        self.master.bind("<Right>", self.player.move_right)
        self.master.bind("<space>", self.shoot)

        self.master.after(1, self.game_loop)

    def shoot(self, event):
        projectile = self.player.shoot()
        if projectile:
            self.projectiles.append(projectile)

    def game_loop(self):
        self.move_enemies()
        self.move_projectiles()

        if self.check_collision():
            self.player.lives -= 1
            if self.player.lives == 0:
                self.game_over()

        self.update_score()
        self.master.after(50, self.game_loop)

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.move()
            enemy_projectile = enemy.shoot()
            if enemy_projectile:
                self.projectiles.append(enemy_projectile)

    def move_projectiles(self):
        for projectile in self.projectiles:
            self.canvas.move(projectile, 0, -10)
            if self.canvas.coords(projectile)[1] < 0:
                self.canvas.delete(projectile)

    def check_collision(self):
        for enemy in self.enemies:
            for projectile in self.projectiles:
                if self.is_collision(projectile, enemy):
                    self.enemies.remove(enemy)
                    self.projectiles.remove(projectile)
                    return True
        return False

    def is_collision(self, obj1, obj2):
        x1, y1, w1, h1 = self.canvas.coords(obj1)
        x2, y2, w2, h2 = self.canvas.coords(obj2.id)

        if (x1 < x2 + w2 and x1 + w1 > x2 and
                y1 < y2 + h2 and y1 + h1 > y2):
            return True
        return False

    def update_score(self):
        score_text = f"Score: {len(self.enemies) * 10}"
        lives_text = f"Lives: {self.player.lives}"
        self.canvas.itemconfig(self.score_text, text=score_text)
        self.canvas.itemconfig(self.lives_text, text=lives_text)

    def game_over(self):
        self.canvas.create_text(275, 200, text="Game Over", font=("Helvetica", 30), fill="red")
        self.master.after(2000, self.master.destroy)


if __name__ == "__main__":
    master = Tk()
    game = Game(master)
    master.mainloop()

