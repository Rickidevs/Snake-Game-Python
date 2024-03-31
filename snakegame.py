import turtle
import time
import random

delay = 0.2

wn = turtle.Screen()
wn.title("Snake game developed by Elvin")
wn.bgcolor("black")
wn.setup(width=600, height=650)
wn.tracer(0) 

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

square_size = 20
turtle.pensize(0.2)
turtle.pencolor("grey")
for y in range(-250, 250 + square_size, square_size):
    for x in range(-230, 230 + square_size, square_size):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(square_size)
            turtle.left(90)
turtle.hideturtle()

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(go_up, "Up") 
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


score = 0
high_score = 0

score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color("white")

def show_score():
    score_turtle.clear()
    score_turtle.penup()
    score_turtle.goto(0, 280)
    score_turtle.write("Score: {}  High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))
    score_turtle.hideturtle()

def spawn_food():
    while True:
        show_score()
        x = random.randint(-230, 230)
        y = random.randint(-250, 250)

        if (x, y) not in [(segment.xcor(), segment.ycor()) for segment in segments]:
            break

    food.goto(x, y)

score_turtle.clear()
score_turtle.penup()
score_turtle.goto(0, 280)
score_turtle.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                   font=("Courier", 24, "normal"))
score_turtle.hideturtle()

while True:
    wn.update()

    if head.xcor() > 230 or head.xcor() < -230 or head.ycor() > 250 or head.ycor() < -250:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        delay = 0.2
    

    if head.distance(food) < 20:
        spawn_food()

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay= delay-0.005
        print("mevcut hiz:" ,delay)
        if delay <= 0.007:
            delay = 0.006
       
        score += 10

        if score > high_score:
            high_score = score

        score_turtle.clear()
        score_turtle.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                           font=("Courier", 24, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    head_coords = (head.xcor(), head.ycor())
    for segment in segments:
        if segment.distance(head) < 20 or head_coords in [(segment.xcor(), segment.ycor()) for segment in segments]:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # clean the segments
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()
            score = 0

            score_turtle.clear()
            score_turtle.write("Score: {}  High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))


    time.sleep(delay)

wn.mainloop()
