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

# Question 1: seinni útgáfan var auðveldari þar sem það er hægt
# að skrifa og prófa litla hluta af kóða án þess að vera með 
# fullklárað forrit
#  
# Question 2: það er mun auðveldara að lesa seinni útgáfuna, þar 
# sem það er minna um endurtekningar og kóðanum er skipt upp 
# í mismunandi hluta

# Question 3: ég losnaði við fullt af endurteknum línum og  
# fannst líka auðveldara að sjá leiðir til að bæta kóðann eftir
# að ég skipti honum upp í functions

def print_directions(position):
    '''prints out possible movements based on current position'''
    if round(position, 1) == 1.1 or round(position, 1) == 2.1:
        print("You can travel: (N)orth.")
    if round(position, 1) == 1.2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    if round(position, 1) == 1.3:
        print("You can travel: (E)ast or (S)outh.")
    if round(position, 1) == 2.2 or round(position, 1) == 3.3:
        print("You can travel: (S)outh or (W)est.")
    if round(position, 1) == 2.3:
        print("You can travel: (E)ast or (W)est.")
    if round(position, 1) == 3.2:
        print("You can travel: (N)orth or (S)outh.")

def is_valid(position, choice):
    '''checks if chosen direction is valid for current position'''
    north = ["n","N", 1.1, 1.2, 2.1, 3.1, 3.2]
    south = ["s","S", 1.2, 1.3, 2.2, 3.2, 3.3]
    west = ["w","W", 2.2, 2.3, 3.3]
    east = ["e","E", 1.2, 1.3, 2.3]
    if choice in north and round(position, 1) in north:
        return "north"
    elif choice in south and round(position, 1) in south:
        return "south"
    elif choice in west and round(position, 1) in west:
        return "west"
    elif choice in east and round(position, 1) in east:
        return "east"
    else:
        return False

def new_position(current, movement):
    '''calculates new position based on current location and movement input'''
    if is_valid(current, movement) == "north":
        current += 0.1
        return current
    if is_valid(current, movement) == "south":
        current -= 0.1
        return current
    if is_valid(current, movement) == "west":
        current -= 1.0
        return current
    if is_valid(current, movement) == "east":
        current += 1.0
        return current

location = 1.1

while round(location, 1) != 3.1:
    print_directions(location)
    move = input("Direction: ")
    while is_valid(location, move) == False:
            print("Not a valid direction!")
            move = input("Direction: ")
    location = new_position(location, move)
else:
    print("Victory!")