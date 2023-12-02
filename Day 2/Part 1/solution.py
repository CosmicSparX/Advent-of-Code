test = """ 
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

# inp = test.strip().split("\n")
inp = open("./in.txt", "r").read().strip().split("\n")

def verify(current_hand):
    red, green, blue = 12, 13, 14
    for key, val in current_hand.items():
        if val > eval(key):
            return False
    
    return True


result = 0
for line in inp:
    game_id = int(line.split(':')[0][5:])
    print("\n", game_id)
    hands = line.split(': ')[1].split('; ')
    for hand in hands:
        current_hand = {k: int(v) for v, k in [x.split(" ") for x in hand.split(', ')]}
        print(current_hand)
        if not verify(current_hand):
            break
    else:
        result += game_id

print("\n\nRESULT =", result)