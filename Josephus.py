import sys


# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    # Is the list empty
    def is_empty(self):
        return self.first is None

    # Append an item at the end of the list
    def insert(self, data):
        node = Link(data)
        self.size += 1
        if self.is_empty():
          self.first = node
          self.last = node
          node.next = node
        else:
          node.next = self.first
          self.last.next = node
          self.last = node

    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):

        current = self.first
        length = self.size
        for i in range(length):
          if current.data == data:
            return current
          current = current.next
        return None

    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data): 
        length = self.size
        current = self.last
        for i in range(length - 1):
              if current.next.data == data:
                    if current.next == self.first:
                           self.first = current.next.next
                    elif current.next == self.last:
                          self.last = current
                    toReturn = current.next
                    current.next = current.next.next
                    self.size -= 1
                    return toReturn
              current = current.next

        return None
                     

    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step):
        current = start
        while step > 0:
          current = current.next 
          step -= 1

        data = current.data 
        next_node = current.next
        self.delete (current.data)

        return data, next_node
        
        '''##### ADD CODE HERE #####'''
        

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''


# Input: Number of soldiers
# Outupt: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):

    newlist = CircularList()
    for i in range(1, num_soldiers + 1):
        newlist.insert(Link(i))

    return newlist

# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):
    deaths = []
    for i in range(my_list.size - 1):
          data, newNode = my_list.delete_after(start_data, step_count)
          start_data = newNode
          deaths.append(data)

    return deaths

    '''##### ADD CODE HERE #####'''


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()
