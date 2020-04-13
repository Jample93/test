import hashlib
import json
from time import time
from urlparse import urlparse
import requests



class Blockchain(object):
 
    def __init__(self):
        self.chain = []
        self.current_transaction= [] # 임시 transaction
        self.nodes = set() # 노드 저장 / 같은 노드라도 한번만 저장
        #genesis block  뉴 블록을 통해서 제네시스 블록에 해쉬를 지정.
        self.new_block(previous_hash=1, proof=100)
					
							
    def new_block(self,proof,previous_hash=None):
        block = {
            'index': len(self.chain)+1,
            'timestamp': time(), #timestampe from 1970
            'transaction': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.current_transaction = []
        self.chain.append(block)
        return block

    

	def new_transaction(self,sender,recipient,amount):  # 장부를 기록
		self.current_transaction.append(
			{
				'sender': sender,  # 송신자
				'recipient': recipient, # 수신자
				'amount': amount # 금액
			}
		)
		return self.last_block['index'] + 1

	def register_node(self, address):
		parsed_url = urlparse(address)
		self.nodes.add(parsed_url.netloc) # netloc attribute! network lockation
	
	def valid_chain(self,chain):
		last_block = chain[0]
		current_index = 1
		
		while current_index < len(chain):
			block = chain[current_index]
			print('%s' % last_block)
			print('%s' % block)
			print("\n---------\n")
			# check that the hash of the block is correct
			if block['previous_hash'] != self.hash(last_block):
				return False
			last_block = block
			current_index += 1
		return True

	def resolve_conflicts(self):
		neighbours = self.nodes
		new_chain = None

		max_length = len(self.chain) # Our chain length
		for node in neighbours:
			tmp_url = 'http://' + str(node) + '/chain'
			response = requests.get(tmp_url)
			if response.status_code == 200:
				length = response.json()['length']
				chain = response.json()['chain']

				if length > max_length and self.valid_chain(chain):
					max_length = length

			if new_chain:
				self.chain = new_chain
				return True

			return False

	# directly access from class, share! not individual instance use it
	
    @staticmethod
	def hash(block):  # hash를 json 자료 형태로 나타냄
		block_string = json.dumps(block, sort_keys=True).encode()

		return hashlib.sha256(block_string).hexdigest()
	@property   #내가 얼마만큼 자료를 짯는지 확인할 수 있음
	def last_block(self):
		return self.chain[-1]

	def pow(self, last_proof):
		proof = 0
		while self.valid_proof(last_proof, proof) is False:
			proof += 1

		return proof

	@staticmethod
	def valid_proof(last_proof, proof):
		guess = str(last_proof + proof).encode()
		guess_hash = hashlib.sha256(guess).hexdigest() #hash값 저장
		return guess_hash[:4] == "0000" # :4 앞 4자리가 0000이면 True


