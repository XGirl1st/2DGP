import turtle
count=0

while(count<=500):
    turtle.penup()
    turtle.goto(0,count)
    turtle.pendown()
    turtle.goto(500,count)
    count+=100

	
count=0

while(count<=500):
    turtle.penup()
    turtle.goto(count,0)
    turtle.pendown()
    turtle.goto(count,500)
    count+=100
