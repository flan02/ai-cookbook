import turtle

# ? ruff library: code formatting, lintern, quick fixes, etc.


def draw_square(turtl, size):
    for i in range(4):
        turtl.forward(size)
        turtl.right(90)


def draw_pattern():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Patter example")
    my_turtle = turtle.Turtle()
    my_turtle.speed(10)
    colors = ["red", "blue", "green", "yellow"]
    for i in range(36):
        my_turtle.color(colors[i % len(colors)])
        draw_square(my_turtle, 100)
        my_turtle.right(10)

    turtle.done()


draw_pattern()

# ruff commands

# ruff check file_name --fix # ! fix errors
# ruff format file_name # - format code
