import turtle
import random
turtle.title("the great race")
screen = turtle.getscreen()
turtle.bgcolor("light pink")
oswald = turtle.Turtle()
oswald.color("green")
oswald.shape("turtle")
oswald.penup()
oswald.goto(-200,100)
clancy = oswald.clone()
clancy.color("blue")
clancy.penup()
clancy.goto(-200,-100)
oswald.goto(300,60)
oswald.pendown()
oswald.circle(40)
oswald.penup()
oswald.goto(-200,100)
clancy.goto(300,-140)
clancy.pendown()
clancy.circle(40)
clancy.penup()
clancy.goto(-200,-100)
die = [1,2,3,4,5,6]
for i in range(20):
  if oswald.pos() >= (300,100):
    print("Oswald Wins!")
    break
  elif clancy.pos() >= (300,-100):
    print("Clancy Wins!")
    break
  else:
    oswald_turn = input("Press 'Enter' to roll the die ")
    die_outcome = random.choice(die)
    print("The result of the die roll is: ")
    print(die_outcome)
    print("The number of steps will be: ")
    print(20*die_outcome)
    oswald.fd(20*die_outcome)
    clancy_turn = input("Press 'Enter' to roll the die ")
    die_outcome = random.choice(die)
    print("The result of the die roll is: ")
    print(die_outcome)
    print("The number of steps will be: ")
    print(20*die_outcome)
    clancy.fd(20*die_outcome)
turtle.done()
