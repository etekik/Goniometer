import math
import turtle

x1 = int(input("Please enter a first x cooedinate: "))
y1 = int(input("Please enter a first y cooedinate: "))
x2 = int(input("Please enter a second x cooedinate: "))
y2 = int(input("Please enter a second x cooedinate: "))
m1 = float(y1 / x1)
m2 = float(abs(y2 - y1) / abs(x2 - x1))
atanx = float(abs(m2 - m1) / abs(1 +(m1 * m2)))
x = math.atan(atanx)
x = x * (180 / math.pi)
turtle.title("Goniometer")

turtle.up()
turtle.goto(0 ,0)
turtle.down()

turtle.goto(x1, y1)
turtle.goto(x2, y2)

turtle.up()
turtle.goto(x1, y1)
turtle.write(x)

turtle.done()