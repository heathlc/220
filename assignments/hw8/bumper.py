"""
Name: Lydia Heath
bumper.py

Problem: Practicing decision statements with graphics.

Certificate of Authenticity:
I certify this work is entirely my own.
"""

from random import randint
import math
from time import sleep
from graphics import Circle, Point, GraphWin, color_rgb


def get_random(int_move_amount):
    return randint(-int_move_amount, int_move_amount)


def did_collide(circle_ball1, circle_ball2):
    ball1_center = circle_ball1.getCenter()
    ball1_x = ball1_center.getX()
    ball1_y = ball1_center.getY()
    ball1_radius = circle_ball1.getRadius()
    ball2_center = circle_ball2.getCenter()
    ball2_x = ball2_center.getX()
    ball2_y = ball2_center.getY()
    ball2_radius = circle_ball2.getRadius()
    distance_eqn = math.sqrt((ball2_x - ball1_x)**2 + (ball2_y - ball1_y)**2)
    radius_eqn = ball1_radius + ball2_radius
    if distance_eqn <= radius_eqn:
        var = bool(True)
    else:
        var = bool(False)
    return var


def hit_vertical(circle_ball, win):
    v_center = circle_ball.getCenter()
    v_x_pos = v_center.getX()
    v_radius = circle_ball.getRadius()
    v_width = win.getWidth()
    if v_x_pos <= v_radius or v_x_pos >= v_width - v_radius:
        var = bool(True)
    else:
        var = bool(False)
    return var


def hit_horizontal(circle_ball, win):
    h_center = circle_ball.getCenter()
    h_y_pos = h_center.getY()
    h_radius = circle_ball.getRadius()
    h_height = win.getHeight()
    if h_y_pos <= h_radius or h_y_pos >= h_height - h_radius:
        var = bool(True)
    else:
        var = bool(False)
    return var


def get_random_color(circle_ball):
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    circle_ball.setFill(color_rgb(red, green, blue))


def main():
    win = GraphWin("Bumpers", 500, 500)
    circle_1 = Circle(Point(100, 250), 20)
    get_random_color(circle_1)
    circle_1.draw(win)
    circle_2 = Circle(Point(400, 250), 20)
    get_random_color(circle_2)
    circle_2.draw(win)
    for _ in range(50):
        sleep(0.4)
        circle_1.move(get_random(100), get_random(100))
        circle_2.move(get_random(100), get_random(100))
        if did_collide(circle_1, circle_2):
            center_1 = circle_1.getCenter()
            circle_1.move(center_1.getX() * -1, center_1.getY() * -1)
            center_2 = circle_2.getCenter()
            circle_2.move(center_2.getX() * -1, center_2.getY() * -1)
        if hit_vertical(circle_1, win):
            v_center_1 = circle_1.getCenter()
            circle_1.move(v_center_1.getX() * -1, v_center_1.getY())
        if hit_vertical(circle_2, win):
            v_center_2 = circle_2.getCenter()
            circle_2.move(v_center_2.getX() * -1, v_center_2.getY())
        if hit_horizontal(circle_1, win):
            h_center_1 = circle_1.getCenter()
            circle_1.move(h_center_1.getX(), h_center_1.getY() * -1)
        if hit_horizontal(circle_2, win):
            h_center_2 = circle_2.getCenter()
            circle_2.move(h_center_2.getX(), h_center_2.getY() * -1)
    win.close()


if __name__ == '__main__':
    main()
