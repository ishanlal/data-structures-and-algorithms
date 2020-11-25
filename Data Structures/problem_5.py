import hashlib
import datetime
class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None
    def __repr__(self):
        return str(self.data)
    def calc_hash(self):
          sha = hashlib.sha256()
          hash_str = self.data.encode('utf-8')
          sha.update(hash_str)
          return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.head = None
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.data) + " -> "
            cur_head = cur_head.next
        return out_string
    def append(self, data):
        if data is None or data == "":
            return
        if self.head is None:
            self.head = Block(datetime.datetime.now(), data, 0)
            return
        node = self.head
        prev = self.head
        while node.next:
            prev = node
            node = node.next
        node.next = Block(datetime.datetime.now(), data, prev.previous_hash)
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size


# Test Block Chains
bc_1 = BlockChain()
bc_2 = BlockChain()
bc_3 = BlockChain()
data_1 = "string 1"
data_2 = "string 2"
data_3 = "string 3"
#Testcase 1
bc_1.append(data_1)
bc_1.append(data_2)
bc_1.append(data_3)
#Testcase 2
bc_2.append("")
bc_2.append("")
#Testcase 3
bc_3.append(None)
bc_3.append(None)
print("BC 1")
print(bc_1) # prints data_1, data_2 and data_3 strings above
print("BC 2")
print(bc_2) # empty string
print("BC 3")
print(bc_3) # empty string
