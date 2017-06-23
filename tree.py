###################################
# Red Black Tree Library
###################################


class Tree:
    """This is my tree class - I hope to make it self balancing, and include an iterator and a backwards iterator"""

    def __init__(self):
        """Constructor"""
        self.root = None
        self.sortedContents = []

    def __iter__(self):
        "Necessary for Tree to be iterable"
        pass

    def insert(self, item):
        """Calls the recursive function insertHelper, which adds the new item"""
        self.root = self.insertHelper(self.root, None, item)

    def insertHelper(self, current_node, node_parent, item):
        """Adds the new item at the correct spot - does not insert it if it is a duplicate"""
        if current_node is None:
            current_node = Node(item, node_parent)
            return current_node

        elif item < current_node.item:
            current_node.left_child = self.insertHelper(current_node.left_child, self, item)
        elif item > current_node.item:
            current_node.right_child = self.insertHelper(current_node.right_child, self, item)
        return current_node

    def displayInOrder(self):
        """Displays the elements in the array in order - this method should get replaced when 
        I make the Tree iterable"""
        self.sortedContents = []
        if self.root is not None:
            self.displayInOrderHelper(self.root)
        print("The tree contains ", end="")
        for item in self.sortedContents[:-1]:
            print(item, end=", ")
        print(self.sortedContents[-1])

    def displayInOrderHelper(self, current_node):
        """Traverses the tree using an inorder traversal, appending items to a list"""
        if current_node.left_child is not None:
            self.displayInOrderHelper(current_node.left_child)
        self.sortedContents.append(current_node.item)
        if current_node.right_child is not None:
            self.displayInOrderHelper(current_node.right_child)

    def begin(self):
        """Returns the first element in the sorted tree"""
        current_node = self.root

        while current_node.left_child is not None:
            current_node = current_node.left_child

        return current_node

    def end(self):
        """Returns the last element in the sorted tree"""
        current_node = self.root

        while current_node.right_child is not None:
            current_node = current_node.right_child

        return current_node

class Node:
    """This class models a node of a binary tree"""
    def __init__(self, item = None, node_parent = None):
        self.item = item
        self.parent = node_parent
        self.left_child = None
        self.right_child = None
