class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""

        start = self.root
        try:
            return self.preorder_search(start, find_val)
        except:
            return False


    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal = []
        try:
            return self.preorder_print(self.root, traversal)
        except:
            pass

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""

        if start.value == find_val :
            print "found", start.value
            return True

        try:
            print "left branch", start.value
            return self.preorder_search(start.left, find_val)

        except:
            print "right branch ", start.value
            return self.preorder_search(start.right, find_val)



    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""

        traversal.append(start.value)
        print traversal
        try:
            self.preorder_print(start.left, traversal)
        except:
            self.preorder_print(start.right, traversal)

        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
# tree.root.left.left.left = Node(7)
# Test search
# Should be True
print tree.search(4)
print "=" * 30
print tree.search(3)
print "=" * 30
# # Should be False
print tree.search(6)
print "=" * 30
print "=" * 30
# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()
