import random
players = ["Andrea", "Colton", "Ariana", "Kayla", "Anthony", "Destiny", "Jeanette",
"Jacque", "Kody", "Kaden", "Kason", "Ashley", "Oswald", "Clancy", "Gilbert", "Marvie", "Alan", "Craig",
"Lexi", "Jack"]
print("Welcome to Team Allocator!!")

while True:
    random.shuffle(players)
    response = input("Is it a team or individual sport?\
        \nType team or individual: ")
    if response == "team":
        team1 = players[:len(players)//2]
        for player in team1:
            print(player)
        team2 = players[len(players)//2:]
        for player in team2:
            print(player)
        print("\nTeam 1 captain: " + random.choice(team1))
        print("Team 1:")
        print("\nTeam 2 captain: " + random.choice(team2))
        print("Team 2:")
    for player in team1:
        print(player)
    for player in team2:
        print(player)
    response = input("Pick teams again? Type y or n: ")
    if response == "n" :
        break
    else: 
        for i in range(0,20,2):
            print(players[i] + " vs " + players[i+1])
            start = random.randrange(i, i+2)
            print(players[start] + " \nstarts")
            