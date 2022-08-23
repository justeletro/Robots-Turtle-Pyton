import turtle

ventana = turtle.Screen()
ventana.setup(960, 540)
ventana.bgpic("robocar4.png")

objeto = turtle.Turtle()
objeto.color("orange")
objeto.width(10)
objeto.penup()
objeto.goto(-100,60)
objeto.pendown()
objeto.dot()

objeto.forward(120)
objeto.dot()

objeto.forward(120)
objeto.dot()

objeto.right(90)
objeto.forward(120)
objeto.dot()

objeto.right(90)
objeto.forward(120)
objeto.dot()


objeto.forward(120)
objeto.dot()
