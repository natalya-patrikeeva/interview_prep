## Technical Interview

### 1.

To efficiently generate anagrams of input string `t`, I used itertools package and list comprehensions. The algorithm first generates a list of all possible character permutations of string letters given the input string. Then we loop over this list to check if any element is a substring of input `s`. The algorithm's efficiency is `O(n*n!)` where `n` is the length of input string `t`. For example, if `t` is `"ad"`, then generating anagrams is `O(2*2)= O(4)`.

### 2.

First, I convert the input string `a` into a list of its letters and generate substrings of input string by combining adjacent letters into a longer and longer elements. For example, if input `a` is `"93138"`, I generate the list of elements to look like `['93','931','9313','93138']`, then shorter list starting from the second element, such as `['31','313','3138']`, and so on. After I generate all the possible substrings, I check if a substring is in fact palindromic by comparing from the beginning and the end of the string and storing the string if it is a palindrom. I compare the size of the palindromatic substring to the newly found palindromic string, keep and return the longest.

The efficiency of the algorithm is `O(n<sup>3</sup>)`, where `n` is the length of input string because of the three `for` loops over `n` elements to generate all the possible substrings and check if they are palindromic. 

### 3.

