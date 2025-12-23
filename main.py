# Import Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400   #Milliseconds

off


def move_snake():
stamper.clearstamps()

new_head = snake[-1].copy()
new_head[0] += 20

# Add new head to the snake's body
snake_append(new_head)

# Remove last segment of the snake
snake.pop(0)

# Create a window to do the drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) #Setting the dimensions of Turtle Graphics window
screen.title("Snake")
screen.bgcolor("magenta")
screen.tracer(0) # Turn off automatic animation

# Event handlers
screen.listen()

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