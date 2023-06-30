import turtle

drawing_board=turtle.Screen()
drawing_board.title("Drawing Board")
drawing_board.bgcolor("light blue")

turtle_instance=turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(20)
def turtle_rotate_right():
    turtle_instance.right(10)
def turtle_rotate_left():
    turtle_instance.left(10)
def turtle_backward():
    turtle_instance.backward(20)
drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="w")
drawing_board.onkey(fun=turtle_rotate_right,key="d")
drawing_board.onkey(fun=turtle_rotate_left,key="a")
drawing_board.onkey(fun=turtle_backward,key="s")
drawing_board.onkey(fun=turtle_forward,key="w")
drawing_board.onkey(fun=turtle_forward,key="w")
drawing_board.onkey(fun=turtle_forward,key="w")
turtle.mainloop()