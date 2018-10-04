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
    if position == 11 or position == 21:
        print("You can travel: (N)orth.")
    if position == 12:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    if position == 13:
        print("You can travel: (E)ast or (S)outh.")
    if position == 22 or position == 33:
        print("You can travel: (S)outh or (W)est.")
    if position == 23:
        print("You can travel: (E)ast or (W)est.")
    if position == 32:
        print("You can travel: (N)orth or (S)outh.")

def is_valid(position, choice):
    '''checks if chosen direction is valid for current position'''
    north = ["n","N", 11, 12, 21, 31, 32]
    south = ["s","S", 12, 13, 22, 32, 33]
    west = ["w","W", 22, 23, 33]
    east = ["e","E", 12, 13, 23]
    if choice in north and position in north:
        return "north"
    elif choice in south and position in south:
        return "south"
    elif choice in west and position in west:
        return "west"
    elif choice in east and position in east:
        return "east"
    else:
        return False

def new_position(current, movement):
    '''calculates new position based on current location and movement input'''
    if is_valid(current, movement) == "north":
        current += 1
        return current
    if is_valid(current, movement) == "south":
        current -= 1
        return current
    if is_valid(current, movement) == "west":
        current -= 10
        return current
    if is_valid(current, movement) == "east":
        current += 10
        return current

def pull_lever(current_loc, coin):
    '''if current location has a lever player can pull it and receive a coin'''
    loc_list = [12, 22, 23, 32]
    if current_loc in loc_list:
        choice = input("Pull a lever (y/n): ")
        if choice.lower() == "y":
            coin += 1
            print("You received 1 coins, your total is now " + str(coin) + ".")
    return coin

def main_game():
    location = 11
    coins = 0

    while location != 31:
        print_directions(location)
        move = input("Direction: ")
        while is_valid(location, move) == False:
                print("Not a valid direction!")
                move = input("Direction: ")
        location = new_position(location, move)
        coins = pull_lever(location, coins)
    else:
        print("Victory!")

choice = "y"
while choice.lower() == "y":
    main_game()
    choice = input("Play again (y/n): ").lower()