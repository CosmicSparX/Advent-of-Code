from collections import defaultdict

test = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# inp = [list(row) for row in test.strip().split("\n")]
inp = [list(row) for row in open("in.txt", "r").read().strip().split("\n")]

nums = dict()

for i in range(len(inp)):
    j = 0
    while j < len(inp[0]):
        if inp[i][j].isdigit():
            key = (i, j)
            num = ""
            while j < len(inp[0]) and inp[i][j].isdigit():
                num += inp[i][j]
                j += 1
            key = (key, (i, j-1))
            nums[key] = int(num)
        j += 1


gears = defaultdict(list)

def find_gear(key, val):
    start_j = key[0][1] - 1 if key[0][1] - 1 > 0 else 0
    end_j = key[1][1] + 1 if key[1][1] + 1 < len(inp[0]) else len(inp[0]) - 1
    start_i = key[0][0] - 1 if key[0][0] - 1 > 0 else 0
    end_i = key[0][0] + 1 if key[0][0] + 1 < len(inp) else len(inp) - 1

    for i in range(start_i, end_i+1):
        for j in range(start_j, end_j+1):
            if inp[i][j] == "*":
                gears[(i, j)].append(val)

for key, val in nums.items():
    find_gear(key, val)
print(gears)

result = 0
for gear_ratio in gears.values():
    if len(gear_ratio) == 2:
        result += gear_ratio[0] * gear_ratio[1]

print("\nResult =", result)