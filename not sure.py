import turtle

turtle.bgcolor("lightskyblue")

scn = turtle.Screen()
grass = turtle.Turtle()
asalt = turtle.Turtle()
houz = turtle.Turtle()
tres = turtle.Turtle()

grass.speed(0.1)
asalt.speed(0.1)
houz.speed(0.1)
tres.speed(0.1)

def makegrass():
    grass.begin_fill()
    grass.color("yellowgreen")
    grass.forward(350)
    grass.right(90)
    grass.forward(350)
    grass.right(90)
    grass.forward(750)
    grass.right(90)
    grass.forward(350)
    grass.right(90)
    grass.forward(400)

    grass.end_fill()

def road():
    asalt.begin_fill()
    asalt.color("gray")
    asalt.forward(350)
    asalt.right(90)
    asalt.forward(50)
    asalt.right(90)
    asalt.forward(750)
    asalt.right(90)
    asalt.forward(50)
    asalt.right(90)
    asalt.forward(400)

    asalt.end_fill()

def house():
    houz.begin_fill()
    houz.color("mediumvioletred")
    houz.forward(100)
    houz.left(90)
    houz.forward(75)
    houz.left(90)
    houz.forward(150)
    houz.left(90)
    houz.forward(75)
    houz.left(90)
    houz.forward(50)
    houz.end_fill()
    houz.left(180)
    houz.forward(50)
    houz.color("magenta")
    houz.begin_fill()
    houz.forward(50)
    houz.right(90)
    houz.forward(75)
    houz.right(90)
    houz.forward(50)
    houz.end_fill()
    houz.color("orange")
    houz.begin_fill()
    houz.forward(10)
    houz.left(135)
    houz.forward(50)
    houz.left(90)
    houz.forward(50)
    houz.left(135)
    houz.end_fill()
    houz.forward(70)
    houz.color("darkorange")
    houz.begin_fill()
    houz.forward(150)
    houz.left(135)
    houz.forward(50)
    houz.left(45)
    houz.forward(150)
    houz.left(135)
    houz.forward(50)
    houz.end_fill()
    houz.left(45)
    houz.forward(10)

def bush(colo, size):
    tres.pendown()
    tres.color(colo)
    tres.begin_fill()
    tres.circle(size)
    tres.end_fill()
    tres.penup()

def treez():
    tres.pendown()
    tres.left(60)
    tres.begin_fill()
    for i in range(20):
        tres.forward(2)
        tres.left(2)
    for i in range(20):
        tres.forward(2)
        tres.left(3)

    tres.right(90)
    tres.forward(10)
    tres.right(90)
    for i in range(25):
        tres.forward(2)
        tres.right(1.5)

    tres.left(140.5)

    for i in range(25):
        tres.forward(2)
        tres.right(1)

    tres.right(90)
    tres.forward(10)
    tres.right(90)

    for i in range(47):
        tres.forward(2)
        tres.left(1)

    tres.end_fill()

    tres.left(165)
    tres.penup()
    tres.forward(100)

    tres.pendown()

    bush("darkgreen", 40)
    tres.right(90)
    tres.forward(30)
    tres.left(90)
    bush("darkgreen", 30)
    tres.left(90)
    tres.forward(20)
    tres.right(90)
    tres.forward(20)
    bush("limegreen", 20)
    tres.right(180)
    tres.right(90)
    tres.forward(40)
    bush("forestgreen", 30)
    tres.left(90)
    tres.forward(120)
    tres.left(90)
    tres.color("brown")
    tres.penup()


makegrass()
grass.penup()
grass.goto(1000, 1000)

asalt.right(90)
asalt.forward(100)
asalt.left(90)

road()
asalt.penup()
asalt.goto(1000, 1000)

houz.right(90)
houz.forward(50)
houz.left(90)

house()
houz.penup()
houz.goto(1000, 1000)

tres.penup()
tres.color("brown")
tres.forward(150)
tres.right(90)
tres.forward(20)
tres.left(90)
tres.pendown()

treez()

tres.goto(-200, -30)
treez()

tres.goto(300, -60)
treez()

tres.goto(-300, -80)
treez()

tres.goto(10, -60)
treez()

tres.goto(-170, -280)
treez()

tres.goto(140, -310)
treez()

tres.penup()
tres.goto(1000, 1000)



turtle.exitonclick()