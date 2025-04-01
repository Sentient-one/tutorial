import turtle

t = turtle.Turtle()
t.speed(5)  


def draw_hexagon(size):
    for _ in range(6):
        t.forward(size)
        t.left(60)
for i in range(10):
    t.penup()
    t.home() 
    t.left(i * 36)  
    t.forward(70) 
    t.pendown()
    

    draw_hexagon(70)
t.hideturtle()
turtle.done()