'''Question 1'''
from collections import Counter

def question1(s, t):
    ''' Given two strings s and t, this function checks wheather
     an anagram of t is a substring of s.
    Inputs: strings s, t
    Output: True or False
    '''
    # Check to see if input string is valid
    if t == None or s == None:
        return "Not a valid input. Please try with a valid string."
    else:

        # Create a dictionary to store letter counts in t
        t = list(t)
        counts_t = Counter(t)

        # Possible substrings of s of varying lengths
        s_substrings = []
        for ii in range(0, len(s)):
            string = s[ii:]
            for i in range(1, len(string)+1):
                s_substrings.append(string[:i])

        # Compare counts of letters in t and in substrings of s
        # If the count is the same, t is an anagram of a substring of s
        for s in s_substrings:
            if counts_t == Counter(s):
                return True
        else:
            return False

# Test
print question1("udacity", "ad")
# Should return True
print question1("udacity", "")
# Should return False
print question1("udacity", None)
# Should return "Not a valid input. Please try with a valid string."

'''Question 2'''
def question2(a) :
    '''Given a string a, find the longest palindromic
     substring contained in a.
     Input: string a
     Output: longest palindromic substring in a'''

    # Check if input is a character string
    if not isinstance(a, basestring):
        return "Not a valid input. a must be a string."
    else:

        # Odd palindromes
        # Loop over centers
        palindrome = ''
        low = 0
        high = 0
        for i in range(1, len(a)-1):
            # Odd palindromes
            low = i-1
            center = a[i]
            high = i+1

            if a[low] == a[high] :
                palindrome = ''.join(a[low] + center + a[high])

                while low > 0 and high <= len(a) and a[low] == a[high] :

                    low -= 1
                    high +=1

                    if a[low] == a[high] :
                        palindrome = ''.join(a[low] + palindrome + a[high])
                    else:
                        break

            # Even palindromes
            low = i-1
            high = i

            if a[low] == a[high]:
                palindrome = ''.join(a[low] + a[high])
                while low > 0 and high <= len(a) and a[low] == a[high] :
                    low -= 1
                    high +=1

                    if a[low] == a[high] :
                        palindrome = ''.join(a[low] + palindrome + a[high])

                    else:
                        break

        return palindrome

# Test
print question2("696531358")
# Should return 53135
print question2("05914418")
# Should return 1441
print question2("")
# Should return ""
print question2(101)

'''Question 3'''
def question3(G):
    '''Given an undirected graph G, find the minimum spanning tree within G.'''
    if G == None or G == {}:
        return None
    else:

        # Array to keep track of known nodes
        known = [False for i in range(len(G))]
        # Array to keep track of weights
        cost = [float('Inf') for i in range(len(G))]
        # Path to assemble the minimum cost spanning tree
        path = [-1 for i in range(len(G))]

        vertex = G.keys()
        vertex = sorted(vertex)   # sort alphabetically
        cost[0] = 0

        index = 0  # start with 'A' node
        while (False in known) :

            known[index] = True
            # Update neighbors
            for v in G[vertex[index]]:
                if known[vertex.index(v[0])] == False and cost[vertex.index(v[0])] > v[1]:
                    cost[vertex.index(v[0])] = v[1]
                    path[vertex.index(v[0])] = index

            # Find cheapest unknown vertex
            minvalue = float('Inf')
            for i in range(len(known)):
                if known[i] == False and cost[i] < float('Inf'):
                    if minvalue > cost[i] :
                        minvalue = cost[i]
                        index = i

        # print 'cost updated', cost
        # print 'vertex array', vertex
        # print 'path ', path

        # Write out the minimum spanning tree
        Ans = {}
        for i, v in enumerate(vertex):
            tmp = []
            for j, p in enumerate(path):
                if p == i:
                    tmp.append( (vertex[j], cost[j] ) )

                    # Check if node is already in the dictionary
                    if vertex[j] in Ans:
                        Ans[vertex[j]].append( ( v, cost[j] ))
                    else:
                        Ans[vertex[j]] = [(v, cost[j])]

            # Check if node is already in the dictionary
            if v in Ans :
                if tmp != []:
                    Ans[v].extend( tmp )
            else:
                Ans[v] = tmp
            # raw_input("Press Enter to continue...")

        return Ans

# Test
G = {'A': [('D', 2), ('E', 4)],
     'B': [('D', 6), ('F', 3)],
     'C': [('F', 4), ('G', 6)],
     'D': [('A', 2), ('B', 6)],
     'E': [('A', 4), ('G', 2), ('H', 2)],
     'F': [('B', 3), ('C', 4), ('G', 4)],
     'G': [('C', 6), ('E', 2), ('F', 4)],
     'H': [('E', 2)]}

print question3(G)
# Should return {'A': [('D', 2), ('E', 4)],
#                'B': [('F', 3)],
#                'C': [('F', 4)],
#                'D': [('A', 2)],
#                'E': [('A', 4), ('G', 2), ('H', 2)],
#                'F': [('B', 3), ('C', 4), ('G', 4)],
#                'G': [('E', 2), ('F', 4)],
#                'H': [('E', 2)]}

print question3(None)
# Should return None

G = {}
print question3(G)
# Should return None

'''Question 4'''
def question4(T, r, n1, n2):
    '''Find the least common ancestor between two nodes
     on a binary search tree.'''

    # Check if input tree is empty
    if T == []:
        return "Input is an empty tree"

    # Check if input nodes are in valid range
    elif r > len(T) or len(T) < n1 or n1 < 0 or len(T) < n1 or n1 < 0:
        return "Input nodes are not valid."

    # All inputs are valid
    else:
        # Check if input nodes are on opposite sides of the root
        # if they are, the least common ancestor is the root node
        if ( n1 > r and r > n2 ) or ( n1 < r and r < n2):
            return r

        # input nodes are on the same side of the root
        else:

            while n1 < r and n2 < r:
                for i, e in enumerate(T[r]):
                    # both nodes are on the left side of the root
                    if i < r and e == 1:
                        r = i
            return r

            while n1 > r and n2 > r:
                for i, e in enumerate(T[r]):
                    # both nodes are on the right side of the root
                    if i > r and e == 1:
                        r = i
            return r

# Test
print question4([[0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                3,
                1,
                4)
# Should return 3

print question4([[0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0]],
                 5,
                 4,
                 0)
# Should return 3

print question4([], 1, 0, 0)
# Should return "Input is an empty tree"

print question4([[0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                8,
                1,
                4)
# Should return "Input nodes are not valid."

'''Question 5'''
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

# def question5(ll, m):
# For testing, pass a linked list as an argument
def question5(ll, m, linked_list):

    '''Finds the element in a singly linked list that's m elements from the end.
    Return the value of the node at that position.'''

    # Check if the linked list is None
    if linked_list == None:
        return "Input linked list is None."
    else:

        # Find the length of the linked list by traversing to the end
        current = ll
        ll_length = 1
        while current.next:
            current = current.next
            ll_length += 1

        if m > ll_length:
            return "Not a valid input. Choose a smaller m value."

        # Traverse the list up to ( length of the list - m ) elements
        current = ll
        for i in range(0, (ll_length - m ) ):
            current = current.next

        return current.data


# Test
# For testing, create a linked list class
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

# Nodes to append to a linked list
n1 = Node(5)
n2 = Node(3)
n3 = Node(2)
n4 = Node(1)
n5 = Node(0)

# Linked List
linked = LinkedList(n1)
linked.append(n2)
linked.append(n3)
linked.append(n4)
linked.append(n5)

print question5(n1, 2, linked)
# Should return 1
print question5(n1, 5, linked)
# Should return 5
print question5(n1, 5, None)
# Should return "Input linked list is None."
print question5(n1, 6, linked)
# Should return "Not a valid input. Choose a smaller m value."
