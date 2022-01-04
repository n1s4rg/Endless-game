locations = {0: "You are sleeping",
             1: "You are walking on a road",
             2: "You are at School",
             3: "You are inside a building",
             4: "You are in a restaurant",
             5: "You are in the forest",
             6: "You are in the Ocean",
             7: "You Finally come to Hell",
             8: "You are at the top of paradise"}


exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0},
         6: {"W": 4},
         7: {"E": 5, "S": 2},
         8: {"N": 2, "E": 4}}


words = {
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W",
    "QUIT": "Q"
}

loc = 4
while True:
    availableExitsArray = []
    for opt in exits[loc].keys():
        availableExitsArray.append(list(words.keys())[list(words.values()).index(opt)])

    availableExits = ", ".join(availableExitsArray)
    print(locations[loc])
    if loc == 0:
        break
    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    if direction in words and words[direction] in exits[loc]:
        loc = exits[loc][words[direction]]
    else:
        print("You cannot go in that direction")
