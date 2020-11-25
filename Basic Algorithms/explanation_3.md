Rearrange Array Elements:

Test cases: Arrays and two numbers summing to a max were provided.

Time Complexity: No sorting algorithm was used. A single traversal through the input array was done. Two subarrays were created. Even though we have a single traversal on the list which is O(n), we do use the in-built max() function which is also O(n). Since nesting is taking place: BigO = O(n^2).

Space Complexity: No recursion takes places. The returned subarrays have the same number of elements of the original array. So, BigO = O(n^2).
