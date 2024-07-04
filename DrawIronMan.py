import turtle

# Setup the screen
turtle.hideturtle()
turtle.bgcolor('black')
turtle.setup(500, 600)
turtle.title("Ironman")
turtle.speed(2)

# Define the Iron Man mask pieces
piece1 = [
    [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20)],
    [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]
]
piece2 = [
    [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210)],
    [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]
]
piece3 = [
    [(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],
    [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220), (0, -220)]
]

# Define the positions for the pieces
piece1Goto = (0, 120)
piece2Goto = (0, -30)
piece3Goto = (0, -220)

def draw_piece(piece, pieceGoto, color):
    turtle.penup()
    turtle.goto(pieceGoto)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(len(piece[0])):
        x, y = piece[0][i]
        turtle.goto(x, y)
    for i in range(len(piece[1])): 
        x, y = piece[1][i]
        turtle.goto(x, y)
    turtle.end_fill()

# Draw the pieces with different colors
draw_piece(piece1, piece1Goto, '#B22222')  # Dark Red
draw_piece(piece2, piece2Goto, '#8B0000')  # Darker Red
draw_piece(piece3, piece3Goto, '#FFD700')  # Gold

# Add some additional details
def draw_eye(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('white')
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

# Draw eyes
draw_eye(-40, 100)
draw_eye(40, 100)

# Draw mouth
turtle.penup()
turtle.goto(-30, 50)
turtle.pendown()
turtle.color('black')
turtle.begin_fill()
turtle.setheading(-30)
for _ in range(2):
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(10)
    turtle.left(120)
turtle.end_fill()

# Hide the turtle and finish
turtle.hideturtle()
turtle.done()
