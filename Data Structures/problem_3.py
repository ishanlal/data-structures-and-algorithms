import sys
from queue import PriorityQueue
from functools import total_ordering
dic_ = {}
class Tree:
    def __init__(self, data=None):
        self.root = Node(data, None, None, None)
    def get_root(self):
        return self.root
    def set_root(self, node):
        self.root = node

@total_ordering
class Node:
    def __init__(self, value=None, freq=None, left=None, right=None):
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def set_left_child(self, node):
        self.left = node
    def set_right_child(self, node):
        self.right = node
    def get_left_child(self):
        return self.left
    def get_right_child(self):
        return self.right
    def has_left_child(self):
        return self.left is not None
    def has_right_child(self):
        return self.right is not None
    def __eq__(self, other):
        return (self.freq == other.freq)
    def __lt__(self, other):
        return (self.freq < other.freq)
def huffman_encoding(data):
    freq_table = dict()
    for i in data:
        if i in freq_table:
            freq_table[i] += 1
        else:
            freq_table[i] = 1
    SL = PriorityQueue()
    K = freq_table.keys()
    for key in K:
        SL.put(Node(key, freq_table[key], None, None))
    tr_ = Tree(None)
    while SL.qsize() > 1:
        low_node_1 = SL.get()
        low_node_2 = SL.get()
        freq_sum = low_node_1.freq + low_node_2.freq
        new_node = Node(None, freq_sum, None, None)
        new_node.set_left_child(low_node_1)
        new_node.set_right_child(low_node_2)
        tr_.set_root(new_node)
        SL.put(new_node)
    ret_tree = SL.get()
    generateEncoding(ret_tree, "")
    ret_encd = ""
    for letter in data:
        ret_encd = ret_encd + dic_[letter]
    return ret_encd, ret_tree

def generateEncoding(root, stringgg):
    if (( not root.has_left_child()) and ( not root.has_right_child()) and root.value != None):
        dic_[root.value] = stringgg
        if stringgg == "":
            dic_[root.value] = "1"
        return
    else:
        if root.has_left_child():
            generateEncoding(root.get_left_child(), stringgg+"0")
        if root.has_right_child():
            generateEncoding(root.get_right_child(), stringgg+"1")

def huffman_decoding(data,tree):
    current = tree
    ret_string = ""
    for i in range(len(data)):
        if (data[i] == '0') :
            if current.has_left_child():
                current = current.get_left_child()
        else:
            if current.has_right_child():
                current = current.get_right_child()
        if ((not current.has_left_child()) and (not current.has_right_child()) ):
            ret_string = ret_string + current.value
            current = tree
    return ret_string

if __name__ == "__main__":
    codes = {}
    # Testcase 1
    data_1 = ""
    a_great_sentence = data_1
    if ((a_great_sentence == None) or (a_great_sentence == "")):
        print("Enter valid data!")
    else:
        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        decoded_data = huffman_decoding(encoded_data, tree)
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
    # Testcase 2
    data_2 = None
    a_great_sentence = data_2
    if ((a_great_sentence == None) or (a_great_sentence == "")):
        print("Enter valid data!")
    else:
        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        decoded_data = huffman_decoding(encoded_data, tree)
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
    # Testcase 3
    data_3 = "The bird is the word"
    a_great_sentence = data_3
    if ((a_great_sentence == None) or (a_great_sentence == "")):
        print("Enter valid data!")
    else:
        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        decoded_data = huffman_decoding(encoded_data, tree)
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
    #Testcase 4
    data_4 = "AAAAAAABBBCCCCCCCDDEEEEEE"
    a_great_sentence = data_4
    if ((a_great_sentence == None) or (a_great_sentence == "")):
        print("Enter valid data!")
    else:
        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        decoded_data = huffman_decoding(encoded_data, tree)
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

    #Testcase 5
    data_5 = "aaaa"
    a_great_sentence = data_5
    if ((a_great_sentence == None) or (a_great_sentence == "")):
        print("Enter valid data!")
    else:
        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print("encoded data {}".format(encoded_data))
        print("tree {}".format(tree))
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        decoded_data = huffman_decoding(encoded_data, tree)
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

    #Testcase 6
    data_6 = "a"
    a_great_sentence = data_6
    if ((a_great_sentence == None) or (a_great_sentence == "")):
        print("Enter valid data!")
    else:
        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        decoded_data = huffman_decoding(encoded_data, tree)
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

    #Testcase 7
    data_7 = "aaaa"
    a_great_sentence = data_7
    if ((a_great_sentence == None) or (a_great_sentence == "")):
        print("Enter valid data!")
    else:
        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        decoded_data = huffman_decoding(encoded_data, tree)
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
