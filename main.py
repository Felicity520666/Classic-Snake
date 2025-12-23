# Import Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 200   #Milliseconds

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left":(-20, 0),
    "right": (20, 0)
}

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"



def move_snake():
    stamper.clearstamps()  #Remove the existing stamps made by stamper

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Add new head to the snake's body
    snake.append(new_head)

    # Remove last segment of the snake
    snake.pop(0)

    # Draw snake the first time
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    # Refresh screen
    screen.update()

    # Rinse and repeat
    turtle.ontimer(move_snake, DELAY)


# Create a window to do the drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) #Setting the dimensions of Turtle Graphics window
screen.title("Snake Game")
screen.bgcolor("magenta")
screen.tracer(0) # Turn off automatic animation

# Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.

# Create a turtle to do the bidding
stamper = turtle. Turtle()
stamper.shape("square")
stamper.penup()

# Create snake as a list of coordinates
snake = [[0,0], [20, 0], [40, 0], [60, 0]]

snake_direction = "up"

# Draw snake the first time
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()


# Set animation in motion
move_snake()
    

# Finish well
turtle.done()