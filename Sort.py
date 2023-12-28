import sys

class SortStats:

    def __init__(self, **kwargs):
        self.sort_type = kwargs.get("sort_type")
        self.numbers = kwargs.get("numbers")
        self.comparisons = 0
        self.swaps = 0
        self.extra_bytes = 0

    def __str__(self):
        return self.sort_type + " Sort Results\nSorted numbers: " + str(self.numbers) +'\nComparisons: ' + str(self.comparisons) +'\nSwaps: ' + str(self.swaps) + "\nExtra Bytes: " + str(self.extra_bytes) + "\n"
            
# Read numbers from input and return them in a list
def get_nums(line):
    return [int(num) for num in line.split()]

# Exchange nums[n] and nums[m]
def swap(nums, n, m):
    nums[n], nums[m] = nums[m], nums[n]  

###############  Zybooks Selction Sort
def selection_sort(numbers):
    curState = SortStats(sort_type="Selection", numbers=numbers)
    for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            curState.comparisons += 1
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
    
        # Swap numbers[i] and numbers[index_smallest]
        curState.swaps += 1
        swap(numbers, i, index_smallest)

    print(curState)

###############  Zybooks Insertion Sort
def insertion_sort(numbers):
    curStats = SortStats(sort_type = "Insertion", numbers=numbers)
    for i in range(1, len(numbers)):
        j = i
        # Insert numbers[i] into sorted part
        # stopping once numbers[i] is in correct position
        while j > 0:
            curStats.comparisons += 1                   
            if numbers[j] < numbers[j - 1]: 
                curStats.swaps += 1   
                swap(numbers, j, j-1)                               
                j -= 1
            else:
                break          

    print(curStats)                

        
##############  Zybooks Merge Sort        
def merge(numbers, i, j, k, curStats):
                 
    merged_size = k - i + 1  
    merged_numbers = []
    for l in range(merged_size):
        curStats.extra_bytes += 4
        merged_numbers.append(0)

    merge_pos = 0                         

    left_pos = i                         
    right_pos = j + 1                   

    while left_pos <= j and right_pos <= k:
        # Added for solution
        curStats.comparisons += 1           
        if numbers[left_pos] < numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos = left_pos + 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos = left_pos + 1
        merge_pos = merge_pos + 1

    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    merge_pos = 0
    while merge_pos < merged_size:
        numbers[i + merge_pos] = merged_numbers[merge_pos]
        merge_pos = merge_pos + 1


def merge_sort(numbers, i, k, curStats):

    j = 0
    if i < k:
        j = (i + k) // 2 

        merge_sort(numbers, i, j, curStats)
        merge_sort(numbers, j + 1, k, curStats)

        merge(numbers, i, j, k, curStats)

        
############## Zybooks Quick Sort
def partition(numbers, i, k, curStats):
    #  Pick middle element as pivot 
    midpoint = i + (k - i) // 2
    pivot = numbers[midpoint]

    #  Initialize variables
    done = False
    l = i
    h = k
    while not done:
        #  Increment l while numbers[l] < pivot 
        while numbers[l] < pivot:
            l = l + 1
        #  Decrement h while pivot < numbers[h] 
        while pivot < numbers[h]:
            h = h - 1
        """  If there are zero or one items remaining,
              all numbers are partitioned. Return h """
        curStats.comparisons += 1
        if l >= h:
            done = True
        else:
            curStats.swaps += 1
            swap(numbers, l, h)      
            l = l + 1
            h = h - 1
    return h


def quick_sort(numbers, i, k, curStats):
    j = 0
    """  Base case: If there are one or zero entries to sort,
          partition is already sorted  """ 
    curStats.comparisons += 1
    if i >= k:
        return
    """  Partition the data within the array. Value j returned
          from partitioning is location of last item in low partition. """ 
    j = partition(numbers, i, k, curStats)
    """  Recursively sort low partition (i to j) and
          high partition (j + 1 to k) """
    quick_sort(numbers, i, j, curStats)
    quick_sort(numbers, j + 1, k, curStats)
    
    return
        

def main():
    # open file
    debug = False
    if debug:
        in_data = open('sort.in')
    else:
        in_data = sys.stdin        
        
    # read each line and analyze, each line is a set of number to sort
    line = in_data.readline()
    while line != "":
        original_nums = get_nums(line)
        print ("########################### New Numbers")
        print(f'##### Original numbers: {original_nums}\n')
        
        # Selection Sort
        nums_to_sort = original_nums.copy()
        selection_sort (nums_to_sort)
        
        # Insertion Sort
        nums_to_sort = original_nums.copy()      
        insertion_sort (nums_to_sort)
        
        # Merge Sort
        nums_to_sort = original_nums.copy()
        curStats = SortStats(sort_type="Merge", numbers=nums_to_sort)
        merge_sort (nums_to_sort, 0, len(nums_to_sort)-1, curStats)
        print(curStats)

        # Quick Sort
        nums_to_sort = original_nums.copy()
        curStats = SortStats(sort_type="Quick", numbers=nums_to_sort)
        quick_sort (nums_to_sort, 0, len(nums_to_sort)-1, curStats)
        print(curStats)

        print()
        line = in_data.readline()


if __name__ == "__main__":
    main()
