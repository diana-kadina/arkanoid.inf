
from tkinter import *
import time
import random


class Ball:
    def __init__(self, canvas, platform, color):
        self.canvas = canvas
        self.platform = platform
        self.id = canvas.create_oval(10, 10, 30, 30, fill=color)
        self.canvas.move(self.id, 250, 150)
        start = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = start[1]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bot = False

    def hit_platform(self, pos):
        platform_pos = self.canvas.coords(self.platform.id)
        if pos[2] >= platform_pos[0] and pos[0] <= platform_pos[2]:
            if pos[3] >= platform_pos[1] and pos[3] <= platform_pos[3]:
                return True
        return

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)  # pos x1, y1, x2, y2
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.hit_bot = True
        if self.hit_platform(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width:
            self.x = -3


class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.platform_width = 350
        self.id = canvas.create_rectangle(0, 0, self.platform_width, 30, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.x1 = self.canvas_width / 2 - self.platform_width /2
        self.y1 = self.canvas_height - 50
        self.canvas.move(self.id, self.x1, self.y1)
        self.x = 0
        self.speed_x = 13

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

    def move_left(self, event):
        if self.x1 + (-1) * self.speed_x >= 0:
            self.x = (-1) * self.speed_x
            self.x1 += self.x
            self.draw()

    def move_right(self, event):
        if self.x1 + self.speed_x <= self.canvas_width - self.platform_width:
            self.x = self.speed_x
            self.x1 += self.x
            self.draw()




tk = Tk()
tk.title("Арканоїд")
tk.resizable(0, 0)
canvas = Canvas(tk, width=400, height=300, bd=0, highlightthickness=0, background='lavender')
canvas.pack()
tk.update()


platform = Platform(canvas, 'royalblue')
ball = Ball(canvas, platform, 'purple')
canvas.bind_all("keyPress-Left", platform.move_left)
canvas.bind_all("keyPress-Right", platform.move_right)
while 1:
    #if ball.hit_bot == False:
    ball.draw()
    platform.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.004)


