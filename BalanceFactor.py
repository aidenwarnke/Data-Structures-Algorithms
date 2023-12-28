import sys


# Node class that defines items in the Tree
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data.lower())
        else:
            self.insert_helper(self.root, data.lower())

    def insert_helper(self, node, data):
        # Compare the new value with the parent node
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_helper(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_helper(node.right, data)

    def getSpaces(self, num):
        spaces = ""
        for i in range(num):
            spaces += "    "
        return spaces

    # # Print the tree
    # def printTree(self):
    #     if (self.root is None):
    #         return
    #     else:
    #         self.printTreeHelper(self.root)

    # def printTreeHelper(self, node, level=0):
    #     if node.right:
    #         self.printTreeHelper(node.right, level+1)
    #     print(self.getSpaces(level), node.data)
    #     if node.left:
    #         self.printTreeHelper(node.left, level+1)

    # Return the integer balance factor of a tree with the given root node.

    # gets the height using DFS
    def getHeight(self, node):
        if node is None:
            return 0
        stack = [(node, 1)]
        max_h = 0
        while stack:
            n, h = stack.pop()
            max_h = max(max_h, h)
            if n.left:
                stack.append((n.left, h + 1))
            if n.right:
                stack.append((n.right, h + 1))
        return max_h

# subtracts right height from left height, assuming there is a height (node =! 0)—note: this is reversed for this assignment
    def balance_factor(self, node):
        if node is None:
            return 0
        l_h = self.getHeight(node.left)
        r_h = self.getHeight(node.right)
        return r_h - l_h


# ------ DO NOT CHANGE BELOW HERE ------ #


def main():
    # data_in = ''.join(sys.stdin.readlines())
    # node = pickle.loads(str.encode(data_in))

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bfactor.in')
    else:
        in_data = sys.stdin

    list = in_data.readline().split(" ")

    myTree = BST()

    for item in list:
        myTree.insert(item)

    # print("Tree: (tree is sideways with root on the left)")
    # myTree.printTree()

    print(myTree.balance_factor(myTree.root))


if __name__ == "__main__":
    main()
