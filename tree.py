###################################
# Red Black Tree Library
###################################

class Tree:
    def __init__(self):
        self.root = None
        self.sortedContents = []

    def insert(self, item):
        self.root = self.insertHelper(self.root, None, item)

    def insertHelper(self, current_node, node_parent, item):
        if current_node is None:
            current_node = Node(item, node_parent)
            return current_node

        elif item < current_node.item:
            current_node.left_child = self.insertHelper(current_node.left_child, self, item)
        elif item > current_node.item:
            current_node.right_child = self.insertHelper(current_node.right_child, self, item)
        return current_node

    def displayInOrder(self):
        self.sortedContents = []
        if self.root is not None:
            self.displayInOrderHelper(self.root)
        print("The tree contains ", end="")
        for item in self.sortedContents[:-1]:
            print(item, end=", ")
        print(self.sortedContents[-1])

    def displayInOrderHelper(self, current_node):
        if current_node.left_child is not None:
            self.displayInOrderHelper(current_node.left_child)
        self.sortedContents.append(current_node.item)
        if current_node.right_child is not None:
            self.displayInOrderHelper(current_node.right_child)

    def begin(self):
        current_node = self.root
        print("current_node is currently at " + str(current_node.item))

        while current_node.left_child is not None:
            current_node = current_node.left_child
            print("current_node is currently at " + str(current_node.item))

        return TreeIter(current_node)


class TreeIter:
    def __init__(self, node):
        self.node = node

    def __iter__(self):
        return self

    def __next__(self):
        # is self.node None?
        if self.node is None:
            return self.node

        # does self.node have a right child?  If so, he's the inorder successor
        if self.node.right_child is not None:
            self.node = self.node.right_child
            while self.node.left_child is not None:
                self.node = self.node.left_child
            return self.node

        temp = self.node
        self.node = self.node.parent

        # is self.node the root?
        if self.node is None:
            return self.node

        # was self.node a left child?
        if temp == self.node:
            return self.node

        while self.node is not None and temp == self.node.right_child:
            temp = self.node
            self.node = self.node.parent

        return self.node

class Node:
    def __init__(self, item = None, node_parent = None):
        self.item = item
        self.parent = node_parent
        self.left_child = None
        self.right_child = None
