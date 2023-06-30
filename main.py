import turtle

drawing_board=turtle.Screen()
drawing_board.title(input("enter the board title: "))
drawing_board.bgcolor(input("enter the board color: "))

turtle_instance=turtle.Turtle()
turtle_instance.color(input("enter the pen color: "))
turtle_instance.pensize(int(input("enter the pen size: ")))
def turtle_forward():
    turtle_instance.forward(20)
def turtle_rotate_right():
    turtle_instance.right(10)
def turtle_rotate_left():
    turtle_instance.left(10)
def turtle_backward():
    turtle_instance.backward(20)
def turtle_Reset():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.clear()
    turtle_instance.pendown()
def turtle_pen_up():
    turtle_instance.penup()
def turtle_pen_down():
    turtle_instance.down()
drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="w")
drawing_board.onkey(fun=turtle_rotate_right,key="d")
drawing_board.onkey(fun=turtle_rotate_left,key="a")
drawing_board.onkey(fun=turtle_backward,key="s")
drawing_board.onkey(fun=turtle_Reset,key="r")
drawing_board.onkey(fun=turtle_pen_up,key="Up")
drawing_board.onkey(fun=turtle_pen_down,key="Down")
turtle.mainloop()