HTTP Router using a trie:

Test case 1: Tests empty values

Test case 2: Tests root, handler, lookup and addition on different input values.

Test case 3: Tests just root value "/"

Time Complexity: The time to insert and lookup paths in a Trie would be the number of words in the path times number of paths. So, BigO = O(n*m), where n = number of entries or URL's & m = length of path or node that's the word between slashes.

Space Complexity: Here instead of storing characters in the trie we are storing path words for each entry. So, BigO = O(n*m), where n = num of paths and m = number of words in path between slashes.
