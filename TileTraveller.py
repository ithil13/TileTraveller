# Asignment 8
# Guðrún Helga Finnsdóttir

# print available directions
# get input for chosen direction
# check if valid direction
# move to new tile
# repeat until tile 3,3 is reached
# print Victory!

# github: https://github.com/ithil13/TileTraveller

location = 1.1
north = ["n","N"]
south = ["s","S"]
west = ["w","W"]
east = ["e","E"]

while round(location, 1) != 3.1:
    if round(location, 1) == 1.1 or round(location, 1) == 2.1:
        print("You can travel: (N)orth.")
        move = input("Direction: ")
        if move in north:
            location += 0.1
        else:
            print("Not a valid direction!")
    if round(location, 1) == 1.2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        move = input("Direction: ")
        if move in north:
            location += 0.1
        elif move in east:
            location += 1.0
        elif move in south:
            location -= 0.1
        else:
            print("Not a valid direction!")
    if round(location, 1) == 1.3:
        print("You can travel: (E)ast or (S)outh.")
        move = input("Direction: ")
        if move in east:
            location += 1.0
        elif move in south:
            location -= 0.1
        else:
            print("Not a valid direction!")
    if round(location, 1) == 2.2 or round(location, 1) == 3.3:
        print("You can travel: (S)outh or (W)est.")
        move = input("Direction: ")
        if move in south:
            location -= 0.1
        elif move in west:
            location -= 1.0
        else:
            print("Not a valid direction!")
    if round(location, 1) == 2.3:
        print("You can travel: (E)ast or (W)est.")
        move = input("Direction: ")
        if move in east:
            location += 1.0
        elif move in west:
            location -= 1.0
        else:
            print("Not a valid direction!")
    if round(location, 1) == 3.2:
        print("You can travel: (N)orth or (S)outh.")
        move = input("Direction: ")
        if move in north:
            location += 0.1
        elif move in south:
            location -= 0.1
        else:
            print("Not a valid direction!")
else:
    print("Victory!")