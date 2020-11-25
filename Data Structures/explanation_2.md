File Recursion

Test case 1: A test directory was provided to the script with subdirectories with files in them.

Test case 2: A test directory was provided to the script with subdirectories with NO files in them.

Test case 3: A test directory was provided to the script with subdirectories with more subdirectories with and without files in them.

Test directory is attached in Zip.

Time Complexity: Recursion was used to traverse the file paths of all subdirectories and files. Since, all files and folders are traversed and printed out to console the BigO = O(n). Sorting was unnecessary and removed in this submission so BigO remains = O(n). Recursion makes the code easy to follow but doesn't reduce the traversal time per se.

Space Complexity: Since the files and folders were printed out to console there was no data structure required to store large amounts of values in memory at any given instance. However, every recursive call made used stack space which is equal to num of recursive calls made => BigO = O(n) = time Complexity in this case.
