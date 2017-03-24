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
    print anagram

    # check if t is in s:
    for i in anagram:

        if i in s:
            return True

    return False

# Test
# Should return True
# print question1("udacity", "ad")
#
# # Should return False
# print question1("udacity", "g")

'''Question 2'''
def question2(a) :
    palydrome = ''
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
                    if len(palydrome) < len(''.join(each) ) :
                        palydrome = ''.join(each)

    return palydrome


# Test
print question2("93138")
print question2("696531358")
