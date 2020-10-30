#!/bin/python3

import turtle
import random

shelly = turtle.Turtle()
turtle.Screen().bgcolor("white")
colors = ["blue", "cyan", "purple", "grey", "pink", "violet", "black"]
shelly.color("cyan")
shelly.speed(0)

def branch():
    i=0
    while i < 3:
        shelly.color(random.choice(colors))
        i=i+1
        j=0
        while j < 3:
            shelly.forward(30)
            shelly.backward(30)
            shelly.right(45)
            j=j+1
        shelly.left(90)
        shelly.backward(30)
        shelly.left(45)
    shelly.right(90)
    shelly.forward(90)

k=0
while k < 8: 
    branch()
    shelly.left(45)
    k=k+1