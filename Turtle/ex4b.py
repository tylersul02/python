#ex4b.py trs
import turtle
w = turtle.Screen()
w.bgcolor("#000000")
a = turtle.Turtle()
a.pencolor("#8135E9")
a.speed(0)
a.width(0.1)
b = turtle.Turtle()
b.pencolor("#E96C35")
b.speed(0)
b.width(0.1)
c = turtle.Turtle()
c.pencolor("#70E935")
c.width(0.1)
c.speed(0)
d = turtle.Turtle()
d.pencolor("#FFFFFF")
d.width(0.1)
d.speed(0)


def v(size):
	for i in range(250):
		d.fd(size)
		d.right(34)
		size = size + 1.5

def x(size):
	for i in range(500):
		a.fd(size)
		a.left(68)
		size = size + 1.5
		
def y(size):
	for i in range(750):
		c.fd(size)
		c.right(102)
		size = size + 1.5
		
def z(size):
	for i in range(1000):
		b.fd(size)
		b.left(128)
		size = size + 1.5
		
v(5)
x(5)
y(5)
z(5)

holdit = input();
