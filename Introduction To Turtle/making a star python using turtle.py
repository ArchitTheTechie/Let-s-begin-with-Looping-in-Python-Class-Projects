import turtle

screen = turtle.Screen()
screen.setup(800, 500)
screen.title("Star")
screen.bgcolor("pink")

board = turtle.Turtle()

for i in range (5):
    board.forward(100)
    board.right(144)


turtle.done()