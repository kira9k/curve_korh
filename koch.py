import turtle
def koch_curve(t,x,depth):
        if x < 3 or depth == 0:
            t.fd(x)
            return
        t.fd(x/3)
        koch_curve(t,x,depth-1)
        t.lt(60)
        koch_curve(t,x,depth-1)
        t.rt(120)
        koch_curve(t,x,depth-1)
        t.lt(60)
        koch_curve(t,x,depth-1)
        t.fd(x/3)

def snowflake(t,x,depth):
    for i in range(3):
        koch_curve(t,x,depth)
        t.rt(120)



t = turtle.Turtle()
t.up()
new_x = -400
new_y = 100
t.goto(new_x, new_y)
t.down()
#koch_curve(t,3,4)
snowflake(t,3,5)
turtle.mainloop()