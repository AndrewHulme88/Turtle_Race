import turtle
import random

is_race_started = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win!? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_started = True

while is_race_started:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_started = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won!! The {winning_color} turtle is the winner!")
            else:
                print(f"You Lost!! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0,10)  
        turtle.forward(random_distance)  

screen.exitonclick()