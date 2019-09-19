#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "black", "red", "blue", "green", "orange", "purple", "black"]

startx = -50
starty = 150
direction = 0

for s in turtle_shapes:
  new_color = turtle_colors.pop()
  t = trtl.Turtle(shape=s)
  t.speed(0)
  t.fillcolor(new_color)
  t.begin_fill()
  t.pensize(2)
  my_turtles.append(t)
  t.end_fill()
  t.pencolor(new_color)
  t.penup()
  t.setheading(direction)
  t.goto(startx, starty)
  t.pendown()   
  t.forward(100)
  startx = t.xcor()
  starty = t.ycor()
  direction = direction - 30

wn = trtl.Screen()
wn.mainloop()