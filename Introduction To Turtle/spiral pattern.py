import turtle

board = turtle.Turtle()

n = 10

for i in range(n * 4):

    board.forward(i * 10)

    board.right(90)

turtle.done()