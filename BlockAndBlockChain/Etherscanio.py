import hashlib
import time
import random


class Block:
    def __init__(self, index, previous_hash, transactions, difficulty):
        self.index = index
        self.timestamp = int(time.time())
        self.transactions = transactions
        self.merkle_root = self.calculate_merkle_root()
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine_block()
        self.miner = f"Miner_{random.randint(1,100)}"
        self.gas_used = random.randint(21000, 100000)

    def calculate_merkle_root(self):
        tx_string = ''.join(self.transactions)
        return hashlib.sha256(tx_string.encode()).hexdigest()

    def calculate_hash(self):
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            self.previous_hash +
            self.merkle_root +
            str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        target = '0' * self.difficulty
        while True:
            block_hash = self.calculate_hash()
            if block_hash.startswith(target):
                return block_hash
            self.nonce += 1

    def print_block(self):
        print("\n==============================")
        print(f"Block Number     : {self.index}")
        print(f"Block Hash       : {self.hash}")
        print(f"Parent Hash      : {self.previous_hash}")
        print(f"Timestamp        : {self.timestamp}")
        print(f"Miner            : {self.miner}")
        print(f"Nonce            : {self.nonce}")
        print(f"Difficulty       : {self.difficulty}")
        print(f"Gas Used         : {self.gas_used}")
        print(f"Merkle Root      : {self.merkle_root}")
        print("Transactions     :")
        for tx in self.transactions:
            print(f"   - {tx}")
        print("==============================\n")


class Blockchain:
    def __init__(self, difficulty=3):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(
            index=0,
            previous_hash="0" * 64,
            transactions=["Genesis Block"],
            difficulty=self.difficulty
        )
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_hash = self.chain[-1].hash
        new_block = Block(
            index=len(self.chain),
            previous_hash=previous_hash,
            transactions=transactions,
            difficulty=self.difficulty
        )
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            block.print_block()


# ---------------------------
# Run the Blockchain
# ---------------------------

if __name__ == "__main__":
    blockchain = Blockchain(difficulty=4)

    blockchain.add_block(["Alice -> Bob (2 ETH)", "Charlie -> Dave (1 ETH)"])
    blockchain.add_block(["Eve -> Frank (3 ETH)"])
    blockchain.add_block(["Bob -> Alice (0.5 ETH)"])

    blockchain.print_chain()
