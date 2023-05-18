import turtle
#import turtle module in this code
t = turtle.Turtle()
t.screen.bgcolor("black") #setting bg color black
t.pensize(2) #setting pensize 2
t.color("green") #setting color green
t.left(90) #setting left 90
t.backward(100) #setting backward 100
t.speed(500) #setting speed 500
t.shape('turtle') #setting shape turtle
def tree(i):
    if i<10:
        return 
    else:
        t.forward(i)
        t.color("orange")
        t.circle(2)
        t.color("brown")
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)

tree(100)
turtle.done()
