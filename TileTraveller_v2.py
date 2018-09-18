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

def print_directions(position):
    '''prints out possible movements based on current position'''
    if round(position, 1) == 1.1 or 2.1:
        print("You can travel: (N)orth.")
    elif round(position, 1) == 1.2:
        print("You can travel: (N)orth or (S)outh or (E)ast.")
    elif round(position, 1) == 1.3:
        print("You can travel: (S)outh or (E)ast.")
    elif round(position, 1) == 2.2 or 3.3:
        print("You can travel: (S)outh or (W)est.")
    elif round(position, 1) == 2.3:
        print("You can travel: (W)est or (E)ast.")
    elif round(position, 1) == 3.2:
        print("You can travel: (N)orth or (S)outh.")

def valid(position, movement):
    '''checks if input is a valid direction'''
    north = ["n","N"]
    south = ["s","S"]
    west = ["w","W"]
    east = ["e","E"]
    if movement in north:
        if position == 1.1 or 1.2 or 2.1 or 3.1 or 3.2:
            return north
    elif movement in south:
        if position == 1.2 or 1.3 or 2.2 or 3.2 or 3.3:
            return south
    elif movement in west:
        if position == 2.2 or 2.3 or 3.3:
            return west
    elif movement in east:
        if position == 1.2 or 1.3 or 2.3:
            return east
    else:
        return False

def new_position(current, movement):
    '''calculates new position based on current location and movement input'''
    if valid(current, movement) == "north":
        current += 0.1
        return current
    elif valid(current, movement) == "south":
        current -= 0.1
        return current
    elif valid(current, movement) == "west":
        current -= 1.0
        return current
    elif valid(current, movement) == "east":
        current += 1.0
        return current


location = 1.1

while round(location, 1) != 3.1:
    print_directions(location)
    move = input("Direction: ")
    while valid(location, move) == False:
            print("Not a valid direction!")
            move = input("Direction: ")
    new_position(location, move)
else:
    print("Victory!")