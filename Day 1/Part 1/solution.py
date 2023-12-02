test = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


# inp = test.split("\n")
inp = open("./in.txt", "r").read().split("\n")

sum_of_calibration = 0

for line in inp:
    start = 0
    end = len(line) - 1
    calibration_val = ["", ""]
    while start <= end:
        if line[start].isdigit():
            calibration_val[0] = line[start]
        else:
            start += 1

        if line[end].isdigit():
            calibration_val[1] = line[end]
        else:
            end -= 1
        
        if calibration_val[0] and calibration_val[1]:
            break

    if (calibration_val[0] + calibration_val[1]).isdigit():
        print(int(calibration_val[0] + calibration_val[1]))
        sum_of_calibration += int(calibration_val[0] + calibration_val[1])

print("\nSum = ", sum_of_calibration)