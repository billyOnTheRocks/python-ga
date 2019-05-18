import hashlib
import json

from time import time
from uuid import uuid4





class Blockchain(object):
    def __init__(self):
        self.chain =[]
        self.current_transactions =[]

        # crteates the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self,proof, previous_hash=None):
        # generates a new block, and adds it to the chain
        '''

        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash:(Optional) <str> Hash of previous Block
        :return:New Block
        '''


        block = {
        'index': len(self.chain) + 1,
        'timestamp': time(),
        'transactions': self.current_transactions,
        'proof': proof,
        'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

    # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        '''

        :param sender:<str> address of the sender
        :param recipient:<str> address of the recipient
        :param amount:<int> Amount
        :return:<int> The index of the block that will hold this transaction
        '''
        # adds a new transaction to the list
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1



    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
