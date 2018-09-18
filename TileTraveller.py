# Asignment 8
# Guðrún Helga Finnsdóttir

# 1 print available directions
# 2 get input for chosen direction
# 3 check if direction is valid
# 4 if not valid repeat 2 and 3 as needed
# 5 move to new tile
# 6 repeat until tile 3,3 is reached
# 7 print Victory!

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
        while move not in north:
            print("Not a valid direction!")
            move = input("Direction: ")
        else:
            location += 0.1
    if round(location, 1) == 1.2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        move = input("Direction: ")
        while move not in north and move not in east and move not in south:
            print("Not a valid direction!")
            move = input("Direction: ")
        if move in north:
            location += 0.1
        if move in east:
            location += 1.0
        if move in south:
            location -= 0.1            
    if round(location, 1) == 1.3:
        print("You can travel: (E)ast or (S)outh.")
        move = input("Direction: ")
        while move not in east and move not in south:
            print("Not a valid direction!")
            move = input("Direction: ")
        if move in east:
            location += 1.0
        if move in south:
            location -= 0.1
    if round(location, 1) == 2.2 or round(location, 1) == 3.3:
        print("You can travel: (S)outh or (W)est.")
        move = input("Direction: ")
        while move not in south and move not in west:
            print("Not a valid direction!")
            move = input("Direction: ")
        if move in south:
            location -= 0.1
        if move in west:
            location -= 1.0
    if round(location, 1) == 2.3:
        print("You can travel: (E)ast or (W)est.")
        move = input("Direction: ")
        while move not in east and move not in west:
            print("Not a valid direction!")
            move = input("Direction: ")
        if move in east:
            location += 1.0
        if move in west:
            location -= 1.0
    if round(location, 1) == 3.2:
        print("You can travel: (N)orth or (S)outh.")
        move = input("Direction: ")
        while move not in north and move not in south:
            print("Not a valid direction!")
            move = input("Direction: ")
        if move in north:
            location += 0.1
        if move in south:
            location -= 0.1
else:
    print("Victory!")