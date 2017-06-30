###################################
# Red Black Tree
# Daniel Craig
###################################


class Tree:
    """This is my tree class - I hope to make it self balancing, and include an iterator and a backwards iterator"""

    def __init__(self):
        """Constructor"""
        self.root = None
        self.sortedContents = []

    def __iter__(self):
        """Necessary for Tree to be iterable"""
        pass

    def insert(self, item):
        """Calls the recursive function insertHelper, which adds the new item"""
        insert_location = self.__find(item)
        if insert_location is None: #No root
            self.root = Node(item, None)
        elif item < insert_location.item:
            insert_location.left_child = Node(item, insert_location)
        else: # it should be that item >= insert_location.item
            insert_location.right_child = Node(item, insert_location)

#        self.root = self.insertHelper(self.root, None, item)
#        find (item) #make this work - only one binary search need exist, that written in find()

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

    def findItem(self, item):
        """This method returns the node where the item is contained, or raises an exception if it is not found"""
        found_location = self.__find(item)

        if found_location is not None and found_location.item == item:
            return found_location
        else:
            raise NotFoundError("The item '" + str(item) + "' was not found!")

    def __find(self, item):
        """This is a find function meant to be used only internally, use findItem for user facing searches"""
        search_node = self.root
        if self.root is not None:
            search_node = self.__findHelper(search_node, item)
        return search_node

    def __findHelper(self, search_node, item):
        """Uses recursion to find node that contains item"""
        if item < search_node.item and search_node.left_child is not None:
            search_node = self.__findHelper(search_node.left_child, item)
        elif item > search_node.item and search_node.right_child is not None:
            search_node = self.__findHelper(search_node.right_child, item)
        return search_node

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
        else:
            print("The tree is empty!")

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


class TreeIterator:
    """The stub of an iterator for the Tree class"""
    def __init__(self, tree=None, item=None):
        self.tree = tree
        self.current_node = tree.find(item)

    def __next__(self):
        pass


class Node:
    """This class models a node of a binary tree"""
    def __init__(self, item=None, node_parent=None):
        self.item = item
        self.parent = node_parent
        self.left_child = None
        self.right_child = None


class NotFoundError(Exception):
    """An exception meant to be thrown when the item is not found by findItem()"""
    def __init__(self, message):
        self.message = message