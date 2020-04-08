# Flappy
flappy bird game

Za sada sam napravio lik ptice i prepreke i kretanje

KOD

from random import
from turtle import
from freegames import vector

bird=vector(0,0)
balls=[]

def tap(x,y):
    up=vector(0,30)#kretanje ptice gore
    bird.move(up)

def inside(point):
    return -200<point.x<200 and -200<point.y<200

def draw(alive):
    clear()

    goto(bird.x,bird.y)

    if alive:
        dot(10,'green')#ako si živ ptica je zelena točka
    else:
        dot(10,'red')#ako si mrtav ptica je crvena točka

    for ball in balls:
        goto(ball.x,ball.y)
        dot(20,'black')#prepreke su crne točke

    update()
