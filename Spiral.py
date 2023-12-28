import sys

# Input: n
# Output:
def get_dimension(in_data):
    pass
    '''##### ADD CODE HERE #####'''
    for line in in_data:
        print(line)
    #return n

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list a spiral
#         if n is even add one to n
def create_spiral(n):
    pass
    '''##### ADD CODE HERE #####'''  
    # adjusting the dimension
    if n % 2 == 0:
        n += 1

    spiral = [[]]

    for i in range(n):
        for j in range(n):
            spiral[i][j] = 0

    center = len(spiral) // 2
    x = center
    y = center
    number = 1

    # setting the center to 1
    spiral[center][center] = number

    # this is the amount of spirals that will be produced
    for i in range(len(spiral)//2):
        y += 1
        number += 1
        spiral[x][y] = number
        for i in range(n - 2):
            x += 1
            number += 1
            spiral[x][y] = number
        for i in range(n - 1):
            y -= 1
            number += 1
            spiral[x][y] = number
        for i in range(n - 1):
            x -= 1
            number += 1
            spiral[x][y] = number
        for i in range (n - 1):
            y += 1
            number += 1
            spiral[x][y] = number


# Input: handle to input file
#        the number spiral
# Output: printed adjacent sums
def print_adjacent_sums(in_data, spiral):
    pass
    '''##### ADD CODE HERE #####'''


# Input: the spiral, the coord of the number 
# Output: returns sum for those in a corner
def in_corner(spiral, coord):
    x = coord[0]
    y = coord[1]
    max_coord = len(spiral) - 1
    total = 0

    if x == 0 and y == 0:
        total += spiral[x][y + 1]
        total += spiral[x + 1][y + 1]
        total += spiral[x + 1][y]
    elif x == max_coord and y == max_coord:
        total += spiral[x][y - 1]
        total += spiral[x - 1][y - 1]
        total += spiral[x - 1][y]
    elif x == 0 and y == max_coord:
        total += spiral[x][y - 1]
        total += spiral[x + 1][y - 1]
        total += spiral[x + 1][y]
    elif x == max_coord and y == 0:
        total += spiral[x - 1][y]
        total += spiral[x - 1][y + 1]
        total += spiral[x][y + 1]

    return total

# Input: the spiral, the coord of the number 
# Output: returns sum for those in the outer 
#         ring
def outer_ring(spiral, coord):
    x = coord[0]
    y = coord[1]
    max_coord = len(spiral) - 1
    total = 0

    if x == 0: #(0,1)
        total += spiral[x][y - 1]
        total += spiral[x + 1][y - 1]
        total += spiral[x + 1][y]
        total += spiral[x + 1][y + 1]
        total += spiral[x][y + 1]
    elif y == 0: #(1,0)
        total += spiral[x - 1][y]
        total += spiral[x - 1][y + 1]
        total += spiral[x][y + 1]
        total += spiral[x + 1][y + 1]
        total += spiral[x + 1][y]
    elif x == max_coord: # (4,1)
        total += spiral[x][y - 1]
        total += spiral[x - 1][y - 1]
        total += spiral[x - 1][y]
        total += spiral[x - 1][y + 1]
        total += spiral[x][y + 2]
    elif y == max_coord: #(1,4)
        total += spiral[x - 1][y]
        total += spiral[x - 1][y - 1]
        total += spiral[x][y - 1]
        total += spiral[x + 1][y - 1]
        total += spiral[x + 1][y]

    return total

# Input: the spiral, the coord of the number 
# Output: returns sum for those in the inner
#         ring
def inner_rings(spiral, coord):
    x = coord[0]
    y = coord[1]
    total = 0

    total += spiral[x - 1][y]
    total += spiral[x - 1][y - 1]
    total += spiral[x][y - 1]
    total += spiral[x + 1][y - 1]
    total += spiral[x + 1][y]
    total += spiral[x + 1][y + 1]
    total += spiral[x][y + 1]
    total += spiral[x - 1][y + 1]

    return total

# Input: the number spiral
#        the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    pass
    '''##### ADD CODE HERE #####'''
    # checks for zero and negatives
    if n < 1:
        return 0
    # checks for numbers greater than the max 
    # inside the number spiral
    if n > len(spiral) ** 2:
        return 0
    
    # number exists, find the coordinates
    coord = []
    for i in range(len(spiral)):
        for j in range(len(spiral)):
            if spiral[i][j] == n:
                coord.append[i]
                coord.append[j]
    
    if in_corner(spiral, coord) != 0:
        return in_corner(spiral, coord)
    elif outer_ring(spiral, coord) != 0:
        return outer_ring(spiral, coord)
    elif inner_rings(spiral, coord) != 0:
        return inner_rings(spiral, coord)    
    

# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # set the input source - change to False before submitting
    debug = True
    if debug:
        in_data = open('spiral.in', 'r')
    else:
        in_data = sys.stdin



    # process the lines of input
    #size = get_dimension(in_data)

    print(type(in_data))

    # create the spiral
    spiral = [[]]
    #spiral = create_spiral(size)
    # use following line for debugging only
    # print_spiral(spiral)

    # process adjacent sums
    #print_adjacent_sums(in_data, spiral)


if __name__ == "__main__":
    main()
