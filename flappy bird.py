from random import*
from turtle import*
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

def move():
    bird.y -=5

    for ball in balls:
        ball.x -=3

    if randrange(10)==0:
        y=randrange(-199,199)
        ball=vector(199,y)
        balls.append(ball)

    while len(balls)>0 and not inside(balls[0]):
        balls.pop(0)#stvaranje lopti(prepreka)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball-bird)<15:
            draw(False)
            return

    draw(True)
    ontimer(move,50)

setup(420,420,370,0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
