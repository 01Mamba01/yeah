import turtle

def draw_fractal_tree(branch_length, t):
    if branch_length < 5:
        return
    else:
        t.forward(branch_length)
        t.right(20)
        draw_fractal_tree(branch_length - 15, t)
        t.left(40)
        draw_fractal_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("green")
    t.width(2)
    t.speed(0)
    t.penup()
    t.setpos(0, -200)
    t.pendown()

    draw_fractal_tree(100, t)

    screen.exitonclick()

if __name__ == "__main__":
    main()
