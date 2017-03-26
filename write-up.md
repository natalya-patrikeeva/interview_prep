## Technical Interview

### 1.

To efficiently generate anagrams of input string `t`, I used itertools package and list comprehensions. The algorithm first generates a list of all possible character permutations of string letters given the input string. Then we loop over this list to check if any element is a substring of input `s`. The algorithm's efficiency is `O(n*n!)` where `n` is the length of input string `t`. For example, if `t` is `"ad"`, then generating anagrams is `O(2*2)= O(4)`.

### 2.

First, I convert the input string `a` into a list of its letters and generate substrings of input string by combining adjacent letters into a longer and longer elements. For example, if input `a` is `"93138"`, I generate the list of elements to look like `['93','931','9313','93138']`, then shorter list starting from the second element, such as `['31','313','3138']`, and so on. After I generate all the possible substrings, I check if a substring is in fact palindromic by comparing from the beginning and the end of the string and storing the string if it is a palindrom. I compare the size of the palindromatic substring to the newly found palindromic string, keep and return the longest.

The efficiency of the algorithm is `O(n<sup>3</sup>)`, where `n` is the length of input string because of the three `for` loops over `n` elements to generate all the possible substrings and check if they are palindromic. 

### 3.

To find the minimum spanning tree in a weighted undirected graph, I implement Prim's algorithm to traverse every node and edge at least once, following this [visualization](https://www.cs.usfca.edu/~galles/visualization/Prim.html). I keep track of what nodes are visited, the weights and the path from one node to another. I loop over all the nodes until we visit all the vertices and edges. The weights are stored in an array and searching through the array for the edge with the minimum weight requires O (|V|<sup>2</sup>) runtime. 

#### 4.

To find the least common ancestor on a BST, I search through the input matrix to find all parents of input nodes and store them in two lists. The root node is appended last. Then I compare entries in the lists to output the earliest common node which is the least common ancestor of two nodes. The efficiency of the algorithm is O (n<sup>2</sup>) because of the two `for` loops over the rows and columns of the input matrix. 

### 5.

To find the element that is `m` elements from the end of a singly linked list, I loop over the linked list once to write the values of the elements to a Python list. Then I find the element's value based on the length of the list and the input `m` value. The efficiency of the algorithm is O(n) where n is the number of elements in the linked list.