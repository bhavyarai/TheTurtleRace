from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=800, height=600)
race_is_on = False

user_bet = screen.textinput(title="Make Your bet.", prompt="Which Turtle will win the race? Enter color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-150, -100, -50, 0, 50, 100, 150]
print(f"Your bet: {user_bet}")
all_turtles = []

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-380, y=y_positions[turtle_index])
    all_turtles.append(tim)

race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            race_is_on = False
            winner = turtle.pencolor()
        step = random.randint(0, 10)
        turtle.forward(step)

if user_bet == winner:
    print(f"You won! The winner is {winner}.")
else:
    print(f"You lose! The winner is {winner}.")

screen.exitonclick()
