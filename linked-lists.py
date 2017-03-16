'''
There isn't a built-in data structure in Python that looks like a linked list.
Thankfully, it's easy to make classes that represent data structures in Python!

Here's the code for an Element, which will be a single unit in a linked list:
'''

class Element(object):

    def __init__(self, value):
        self.value = value
        self.next = None

# Now, let's set up a LinkedList class:

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):

        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        try:
            for i in range(1, position):
                current = current.next
        except:
            current = None

        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        current = self.head

        # Insert at the end of the list
        if self.get_position(position ) == None:
            # print "inserting at the end of the list: "
            self.append(Element(new_element.value))

        # Insert at the beginning of the list
        elif self.get_position(position).value == 1:
            # print "inserting at head position:"
            new  = new_element
            value_after = self.head
            self.head = Element(new.value)
            self.head.next = value_after


        else:
            # print "inserting in the middle: "
            for i in range(1, ( position - 1 ) ):
                current = current.next

            value_after = current.next
            new  = new_element
            current.next = Element(new.value)
            current.next.next = value_after

        # print "linked list after insert"
        # current = self.head
        # while current.next:
        #     print current.value
        #     current = current.next
        # print current.value

    def delete(self, value):
        """Delete the first node with a given value."""

        current = self.head
        position = self.get_position(value).value

        # Deleting head
        if current.value == value:
            # print "deleting the head of the list"
            self.head = current.next

        # Deleting from the end of the list
        elif self.get_position(position + 1) == None:
            # print "deleting from the end of the list"
            while current.next:
                current = current.next

            current = self.get_position(position - 1)

            # Unlink from previous to current (last item in the list)
            current.next = None

        else:
            # print "deleting from the middle"
            while current.next:
                if current.value == value:

                    before = self.get_position(position - 1)
                    after = current.next
                    current = before
                    current.next = after

                current = current.next

        # print "linked list after delete"
        # current = self.head
        # while current.next:
        #     print current.value
        #     current = current.next
        # print current.value


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
