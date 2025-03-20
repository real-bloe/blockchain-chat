import hashlib
import json
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(data="Genesis Block", sender="System")

    def create_block(self, data, sender):
        previous_hash = self.chain[-1]['hash'] if self.chain else "0"
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'data': data,
            'sender': sender,
            'previous_hash': previous_hash
        }
        block['hash'] = self.hash(block)
        self.chain.append(block)
        return block

    def hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_chain(self):
        return self.chain
