class Contestant:
  def __init__(self, name, input_hobbies, input_age, input_height, input_work, input_social=True, is_tall=True, is_bachelorette = False):
    self.name = name
    self.hobbies = input_hobbies
    self.age = input_age
    self.height = input_height
    self.work = input_work
    self.is_social = input_social
    self.is_tall = is_tall
    self.is_bachelorette = is_bachelorette
    self.points = 0

  def __repr__(self):
    if self.is_bachelorette:
      description = """This is {name}, our Bachelorette looking for her perfect man. \nShe is {age}, {height}, likes to {hobbies}, watch indie horror films and is a {work}. """.format(name=self.name, age=self.age, hobbies=self.hobbies, height=self.height, work=self.work)
    else:
      description = """This is {name}, one of our contestants looking for his dream girl. \nHe is {age}, {height}, likes to {hobbies} and he is a {work}. """.format(name=self.name, age=self.age, hobbies=self.hobbies, work=self.work, height=self.height)

    if self.is_social and self.is_bachelorette:
      description += """\n{name} is very social, she loves to talk about anything and everything and wants someone who can keep up.\n""".format(name=self.name)
    elif not self.is_social and self.is_bachelorette:
      description += """{name} is not very social, she'd much rather spend her nights inside watching her favorite movies with her dream man.""".format(name=self.name)

    if self.is_social and not self.is_bachelorette:
      description += """\n{name} is very social.\n""".format(name=self.name)
    elif not self.is_social and not self.is_bachelorette:
      description += """\n{name} is not very social.\n""".format(name=self.name)
    return description

class Bachelorette(Contestant):
  pass

bachelorette = Bachelorette("Jaleesa", "gossip, study the stars", 22, 66, "Marketing Manager", is_bachelorette=True)
contestants = []
contestants.append(Contestant("Ryan", "read, or Go to a coffee shop to people watch", 25, 75, "Artist", input_social=False, is_tall=True))
contestants.append(Contestant("Fred", "watch anime, and practice Karate", 23, 73, "Freelance Writer", is_tall=False))
contestants.append(Contestant("Eddy", "program, donate to charities", 24, 72, "Scholar and CEO of GitHub", is_tall=True))
contestants.append(Contestant("Josh",  "drink Soda, His favorite flavor is Grape..", 27, 68, "Unemployed couch surfer",is_tall=False))
contestants.append(Contestant("Jordan", "tutor on his free time", 28, 69, "Astronaut for NASA", is_tall=False))

print(bachelorette)
for contestant in contestants:
  points = contestant.height - bachelorette.height
  contestant.points += points
contestants.sort(key=lambda x: x.height, reverse=True)
print(contestants)
# week one, intro to characters and sorting based off height
print("\nWeek One.\n")
first_elimination = contestants.pop(-1)
print("{name} was eliminated first this week. He was shortest in the Height challenge, Thus scoring lowest and will now be going home. Bye {name}!\n".format(name=first_elimination.name))
for contestant in contestants:
  print("{name} has {points} points to end this week.".format(name=contestant.name, points=contestant.points))
# week two, sorting based off if social
print("\nWeek Two.\n")
for contestant in contestants:
  points = contestant.is_social - bachelorette.is_social
  contestant.points += points
contestants.sort(key=lambda item: (not item.is_social))
second_elimination = contestants.pop(-1)
print("{name} was eliminated second this week. He was lowest scored in the social challenge, and will now be going home. Bye {name}!\n".format(name=second_elimination.name))
for contestant in contestants:
  print("{name} has {points} points to end this week.".format(name=contestant.name, points=contestant.points + 2))
# week three, sorting based off age
print("\nWeek Three.\n")
for contestant in contestants:
  points = contestant.age - bachelorette.age
  contestant.points += points
contestants.sort(key=lambda x: x.age)
third_elimination = contestants.pop(-1)
print("{name} was eliminated third this week. He was oldest of the bunch and our bachelorette prefers them younger, He will now be going home. Bye {name}!\n".format(name=third_elimination.name))
for contestant in contestants:
  print("{name} has {points} points to end this week.".format(name=contestant.name, points=contestant.points + 3))
# fourth final week, sorting based off
print("\nWeek Four, Our final challenge and ceremony.\n")
print("This week is based off of Jaleesa's pick, Only two contestants stand before her..Let us see what happens next..\n")
final_elimination = contestants.pop(0)
print("Jaleesa: Both of you have amazing qualities, and special in your own way. But only one can win today.. {name} You have an amazing personaloty, but is that enough? \n".format(name=final_elimination.name))
for contestant in contestants:
  print("Jaleesa: {name} You're charitable, handsome, and tall. But you talk about your mom.. a lot. However, I love a mama's boy. {name} YOU ARE THE WINNER\n".format(name=contestant.name))
  print("Congratulations {name} you are this years season winner! Well, thats all for now folks. Tune in next year for an all new season.".format(name=contestant.name))
