Search in a Rotated Sorted Array:

Test cases: Rotated sorted arrays were inserted with search numbers on both sides of the pivot and search numbers not present in the whole array.

Time Complexity: Binary search used to search the input array for the input number and detect pivot. Binary search time complexity is O(log(n)). So, BigO = O(log(n)).

Space Complexity: Binary search reduces the search space into half every time but the recursive call uses memory for all array elements every time so Space complexity is also O(log(n)).
