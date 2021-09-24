import turtle
from math import atan

turtle.shape('turtle')


def f(a):
    angle = 0
    x = 0
    y = 0
    v_x = 10
    v_y = 10
    t = 0
    for i in range(a):
        while y >= 0:
            turtle.left(angle)
            turtle.forward(y)
            v_y = v_y - 10 * t
            angle = atan(v_y / v_x)
            x = x + v_x * t
            y = y + v_y * t - 10 * t ** 2 / 2
            turtle.goto(x, y)
            t = t + 1
        v_y *= 0.7
        v_x *= 0.7


f(int(input()))
