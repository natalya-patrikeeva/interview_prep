'''Question 1'''
from itertools import permutations
def question1(s, t):
    ''' Given two strings s and t, this function checks wheather an anagram
    of t is a substring of s.
    Inputs: s, t
    Output: True or False
    '''
    # anagrams of t
    t_anagrams = [list(x) for x in permutations(t, len(t) ) ]
    anagram = ["".join(x) for x in t_anagrams ]
    # print anagram
    if t == "":
        return False
    else:
        # check if t is in s:
        for i in anagram:

            if i in s:
                return True

        return False

# Test
print question1("udacity", "ad")
# Should return True
print question1("udacity", "g")
# Should return False
print question1("udacity", "")
# Should return False


'''Question 2'''
def question2(a) :
    '''Given a string a,
    find the longest palindromic substring contained in a.'''
    palindrome = ''
    a_list = list(a)
    for i in range(0, len(a)-1):
        i_list = a_list[i:]

        # dummy lists
        l = list()
        mst_list = list()

        for j in range(0, len(i_list)):
            l.append(i_list[j])
            elm = ''.join(l)
            mst_list.append(elm)

        mst_list.pop(0)

        # Check if element is a palindrom
        for each in mst_list:
            each  = list(each)

            for i in range(0, len(each)-1):
                if each[i] != each[len(each) - 1] :
                    break
                else:
                    # Check if new palindrom is longer than the last
                    if len(palindrome) < len(''.join(each) ) :
                        palindrome = ''.join(each)

    return palindrome

# Test
print question2("93138")
# Should return 313
print question2("696531358")
# Should return 53135
print question2("")
# Should return ""


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
G = {'A': [('B', 2)],
     'B': [('A', 2), ('C', 5)],
     'C': [('B', 5)]}
print question3(G)
# Should return {'A': [('B', 2)],
#                'B': [('A', 2), ('C', 5)],
#                'C': [('B', 5)]}


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

'''Question 4'''
def question4(T, r, n1, n2):
    '''Find the least common ancestor between two nodes
     on a binary search tree.'''

    if T == []:
        return "Input is an empty tree"
    else:
        n1_list = []
        n2_list = []
        while n1 != n2:

            for i in range(len(T)):
                for ii, v in enumerate(T[i]):
                    # find parents of n1 and n2
                    if ii == n1 and v == 1:
                        n1 = i
                        n1_list.append(n1)
                    if ii == n2 and v == 1:
                        n2 = i
                        n2_list.append(n2)

        # Search for least common ancestor
        for n in n1_list:
            if n in n2_list:
                n1 = n
                break
        return n1

# Test
print question4([[0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                3,
                1,
                4)
# Should return 3

print question4([[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0]],
                 5,
                 6,
                 2)
# Should return 2

print question4([], 1, 0, 0)
# Should return "Input is an empty tree"

'''Question 5'''
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

# def question5(ll, m):
# For testing, pass a linked list as an argument
def question5(ll, m, list):

    '''Finds the element in a singly linked list that's m elements from the end.
    Return the value of the node at that position.'''

    stack = []
    current = ll
    while current.next:
        stack.append(current.data)
        current = current.next
    stack.append(current.data)
    if m > len(stack):
        return "Not a valid input. Choose a smaller m value."

    return stack[ len(stack) - m ]

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
print question5(n1, 6, linked)
# Should return "Not a valid input. Choose a smaller m value."
