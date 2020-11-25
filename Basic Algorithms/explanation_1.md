Square Root of an Integer:

Test cases: Base cases of 0 and 1 are tested. Then a few perfect squares were tested. Then non perfect squares were tested to give the floor of the closest perfect square.

Time Complexity: Binary search's time complexity is BigO = O(log(n)). We need to guess the number whose square value reaches but is lower than the input number to get the square root. So, BigO = O(log(n)).

Space Complexity: We are not traversing anything nor recursing the function on the stack so BigO = O(1).
