import turtle

# Set up the screen
window = turtle.Screen()
window.title("Breakout")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]

for y in range(5):
    for x in range(8):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[y])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(-280 + x * 70, 250 - y * 25)
        bricks.append(brick)

# Paddle movement
def move_left():
    x = paddle.xcor()
    if x > -240:
        paddle.setx(x - 20)

def move_right():
    x = paddle.xcor()
    if x < 240:
        paddle.setx(x + 20)

# Keyboard bindings
window.listen()
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        # Reset the ball if it goes below the paddle
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.ycor() < -240 and -50 < ball.xcor() - paddle.xcor() < 50):
        ball.sety(-240)
        ball.dy *= -1

    # Brick and ball collisions
    for brick in bricks:
        if brick.distance(ball) < 20:
            brick.goto(1000, 1000)  # Move the brick off-screen
            ball.dy *= -1

    # Check if all bricks are destroyed
    if all(brick.xcor() == 1000 for brick in bricks):
        window.bye()  # Close the game if all bricks are destroyed
