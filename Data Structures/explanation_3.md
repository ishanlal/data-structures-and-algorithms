Huffman Coding: This took me 2 days to figure out because of python 3 compatibility issues with python 2 while using the PriorityQueue sort/cmp functionality. This problem took quite a lot of thought. Even though I understood the problem description when I read it.

Test case 1: An empty string

Test case 2: An None string

Test case 3: A sentence string

Time Complexity: The string was read into a dictionary to count each unique elements frequency. The dictionary elements were then pushed into a Node class that was put into a PriorityQueue to build the huffman tree. huffman_encoding and huffman_decoding were done recursively. The PriorityQueue has a time complexity of O(log n) for insertion and extraction. The frequency dictionary has a BigO = O(1) for lookups. For N elements in the input data string the process needs to be done N times so BigO = O(nlogn).

Space Complexity: Running a couple of strings through the algorithm we see that a 25 character string size is 74 which is encoded to a size of 32 which is 2.3 times smaller. The sample string sentence also encoded to a size appox 2 times the data size. Thus, we can say that the encoded data size is appox half of the input data size. When decoded the size and content remain the same so we know our algorithm is working fine. So, BigO  = O(data_size(n)/2).
