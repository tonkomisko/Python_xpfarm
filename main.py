import time
import turtle
from planets_2 import Planet


screen = turtle.Screen()
screen.bgpic('./stars.jpg')
screen.tracer(50)

sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')

mercury = Planet("Mercury", 40, 'grey')
venus = Planet("Venus", 80, 'orange')
earth = Planet('Earth', 100, 'blue')
mars = Planet('Mars', 150, 'red')
jupiter = Planet('Jupiter', 180, 'brown')
saturn = Planet('Saturn', 230, 'pink')
uranus = Planet('Uranus', 250, 'light blue')
neptune = Planet('Neptune', 280, 'gray')

solarSystem = [mercury, venus, earth, mars, jupiter, saturn, uranus,
               neptune]

# indefinite while loop, first move all planets, then change the angles and move again
while True:
    time.sleep(0.01)
    # pause refreshing the screen every 0.01 second
    screen.update()
    for i in solarSystem:
        i.move()

    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007
    jupiter.angle += 0.02
    saturn.angle += 0.018
    uranus.angle += 0.016
    neptune.angle += 0.005

# screen.exitonclick()
