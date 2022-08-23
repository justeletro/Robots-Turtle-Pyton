import turtle

ventana = turtle.Screen()
ventana.setup(960, 540)
ventana.bgpic("robocar5.png")

objeto = turtle.Turtle()
objeto.color("orange")
objeto.width(10)
objeto.penup()
objeto.goto(-240,120)
objeto.pendown()
objeto.dot()

objeto.forward(120)
objeto.dot()

objeto.forward(120)
objeto.dot()

objeto.right(90)
objeto.forward(120)
objeto.dot()

objeto.forward(120)
objeto.dot()

objeto.left(90)
objeto.forward(120)
objeto.dot()


objeto.left(90)
objeto.forward(120)
objeto.dot()

objeto.forward(120)
objeto.dot()

objeto.right(90)
objeto.forward(120)
objeto.dot()
