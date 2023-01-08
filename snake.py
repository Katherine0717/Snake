import numpy as np

# Snake head
HEAD = 0

FOOD = 0

HEIGHT = 10
WIDTH = 20
AREA = HEIGHT * WIDTH

LEFT = -1
RIGHT = 1
UP = -WIDTH
DOWN = WIDTH

board = [0] * AREA # 一维数组表示二维数组
snake = [0] * (AREA + 1)
snake_size = 1
snake[HEAD] = 1*WIDTH+1 # 蛇初始位置: [1, 1]

move = [LEFT, RIGHT, UP, DOWN]
score = 1