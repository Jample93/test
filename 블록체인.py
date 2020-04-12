
import datetime as date
import hashlib as hasher
class Block:
def __init__(self, idx, ts, mydata, backhash):
self.idx = idx
self.ts = ts
self.mydata = mydata
self.backhash = backhash
self.hash = self.hashop()
def hashop(self):
shahash = hasher.sha256()
shahash.update(str(self.idx) + str(self.ts) + str(self.mydata) + str(self.backhash))
return shahash.hexdigest()
def genesis():
return Block(0, date.datetime.now(), “Genesis Block”, “0”)
def next_block(last_block):
this_idx = last_block.idx + 1
this_ts = date.datetime.now()
this_mydata = “Block” + str(this_idx)
this_hash = last_block.hash
return Block(this_idx, this_ts, this_mydata, this_hash)
blockchain = [genesis()]
back_block = blockchain[0]
maxblocks = 20
for i in range(0, maxblocks):
block_to_add = next_block(back_block)
blockchain.append(block_to_add)
back_block = block_to_add
print “Block #{} inserted in Blockchain”.format(block_to_add.idx)
print “Hash Value: {}\n”.format(block_to_add.hash)