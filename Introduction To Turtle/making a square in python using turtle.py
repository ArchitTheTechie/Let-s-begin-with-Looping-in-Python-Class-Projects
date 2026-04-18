import turtle

screen = turtle.Screen()
screen.setup(800, 500)
screen.title("Test Screen")
screen.bgcolor("pink")

board = turtle.Turtle()

for i in range(4) :
    board.forward(100)
    board.right(90)


turtle.done()