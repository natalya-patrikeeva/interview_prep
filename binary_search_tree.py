class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.recursive_insert(self.root, new_val)

    def recursive_insert(self, start, new_val):
        if start > new_val:
            while start.left:
                return self.recursive_insert(start.left, new_val)
            start.left = Node(new_val)

        else:
            while start.right:
                return self.recursive_insert(start.right, new_val)
            start.right = Node(new_val)


    def search(self, find_val):
        return self.recursive_search(self.root, find_val)

    def recursive_search(self, start, find_val):

        if find_val == start.value:
            return True

        elif start > find_val:
            while start.left:
                return self.recursive_search(start.left, find_val)
            return False

        else:
            while start.right:
                return self.recursive_search(start.right, find_val)
            return False


    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
print tree.print_tree()

tree.insert(1)
print tree.print_tree()

tree.insert(3)
print tree.print_tree()

tree.insert(5)
print tree.print_tree()

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
