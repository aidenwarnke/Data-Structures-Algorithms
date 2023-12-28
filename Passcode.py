import math
import sys


# Input: a list of integers representing the sequence of numbers in a password, 
# len(ptrn) >= 2
# Output: distance traveled on the number pad
def get_distance(pattern):
    totalDistance = 0
    lastRow, lastCol = find_in_keypad(pattern[0])
    for i in range(1, len(pattern)):
        row, col = find_in_keypad(pattern[i])
        rowDif = abs(lastRow - row)
        colDif = abs(lastCol - col)
        distance = math.sqrt(colDif ** 2 + rowDif ** 2)
        totalDistance += distance

        lastRow, lastCol = row, col


    return totalDistance
        


# DO NOT Edit Below This Line, except for changing the debug variable when you are done


#  Find the equivilant x,y based on grid concept
def find_in_keypad (num):
    row = (num - 1) // 4
    col = (num - 1) % 4
    return (row, col)

# take an inpuyt string and create a list of numbers
def get_pattern (line):
    input_pattern = []
    line = line.split()
    for element in line:
        input_pattern.append(int(element))
    return input_pattern
    
# run the program
def main():
    
    # open file
    debug = False
    if debug:
        in_data = open('passcode.in')
    else:
        in_data = sys.stdin

    # read and process each line until EOF
    line = in_data.readline()
    while line != "":
        pattern = get_pattern(line)
        print(f'Pattern: {pattern}')
        print("Distance: {:.2f}".format(get_distance(pattern)))
        print()
        line = in_data.readline()

if __name__ == "__main__":
    main()
