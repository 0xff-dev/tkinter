import threading
import queue
import time
from tkinter import *
from random import randint


def get_point(x, y):
    return x, y, x+10, y+10


def is_rect_overlap(p1, p2):
    return not(p1[0]+10<p2[0] or p1[1]+10<p2[1] or
            p2[0]+10<p1[0] or p2[1]+10<p1[1])


class Window(Tk):
    def __init__(self, width, height, queue: queue.Queue):
        super(Window, self).__init__()
        self.q = queue
        self.w, self.h = width, height
        self.is_game_over = False
        self.canvas = Canvas(self, width=self.w, height=self.h, bg="#fff")
        self.canvas.pack()
        self.queue_handle()

    def _draw(self, data, color: str):
        for _data in data:
            self.canvas.create_rectangle(get_point(*_data), fill=color, outline="")

    def queue_handle(self):
        try:
            while True:
                task = self.q.get(block=False)
                if task[0] == 'game_over':
                    self.stop()
                if task[0] == 'move':
                    self._draw(task[1], 'green')
        except Exception as _:
            if not self.is_game_over:
                self.canvas.after(100, self.queue_handle)

    def stop(self):
        self.is_game_over = True


class Snake(threading.Thread):
    """单独的线程处理按键"""

    def __init__(self, window: Window, queue: queue.Queue):
        super(Snake, self).__init__()
        self.window = window
        self.queue = queue
        self.daemon = True
        self.snake = [(10, 0), (20, 0), (30, 0)]
        self.dir = 'Right'
        self.food = Food(self.window, self.queue)
        self.start()

    def run(self):
        if self.window.is_game_over:
            self._delete()
        while not self.window.is_game_over:
            self.queue.put(('move', self.snake))
            time.sleep(0.5)
            self.move()

    def key_press(self, event):
        self.dir = event.keysym

    def _next_point(self):
        now_x, now_y = self.snake[-1]
        if self.dir == 'Left':
            now_x = now_x-10
        if self.dir == 'Up':
            now_y = now_y-10
        if self.dir == 'Right':
            now_x = now_x+10
        if self.dir == 'Down':
            now_y = now_y+10
        return now_x, now_y

    def move(self):
        np = self._next_point()
        print('snake head: ', np)
        width, height = self.window.w, self.window.h
        if np in self.snake or np[0] < 0 or np[0] >= width or np[1] < 0 or np[1] >= height:
            self.queue.put(('game_over', True))
        else:
            if not is_rect_overlap(np, self.food.pos):
                pos = self.snake[0]
                self.snake.pop(0)
                self.window.canvas.create_rectangle(get_point(*pos), fill='white', outline='')
            else:
                self.food.gen_point()
            self.snake.append(np)


class Food(object):
    def __init__(self, window: Window, queue: queue.Queue):
        self.window = window
        self.queue = queue
        self.pos = (0, 0)
        self.gen_point()

    def gen_point(self):
        """注意蛇身的位置"""
        self.window.canvas.create_rectangle(get_point(*self.pos), fill='white', outline="")
        self.pos = randint(0, self.window.w), randint(0, self.window.h)
        print("new pos: ", self.pos)
        self.window.canvas.create_rectangle(get_point(*self.pos), fill='red', outline='')


q = queue.Queue()
w = Window(500, 500, q)
w.title = '贪吃蛇'
snake = Snake(w, q)
w.bind('<Key-Left>', snake.key_press)
w.bind('<Key-Right>', snake.key_press)
w.bind('<Key-Up>', snake.key_press)
w.bind('<Key-Down>', snake.key_press)
w.mainloop()
