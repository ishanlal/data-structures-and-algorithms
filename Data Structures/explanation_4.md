Active Directory

Test case 1: valid user string

Test case 2: Empty string

Test case 3: None string

Time Complexity: The userid's are supposed to be unique and are stored in lists. Group's an object with two lists one for users and one for groups. The same set of users could be under different group names thus making them repetitive. The search time to look in a list is O(n). So, Big O = O(n).

Space Complexity: The recursive call is made only if more groups exist under the current group. So BigO = O(n).
