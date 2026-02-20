import hashlib
import time
import random


# ---------------------------
# Block Class
# ---------------------------

class Block:
    def __init__(self, index, data, previous_hash, validator):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.validator = validator
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            self.previous_hash +
            self.validator
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return (
            f"\nBlock Index : {self.index}\n"
            f"Validator   : {self.validator}\n"
            f"Timestamp   : {self.timestamp}\n"
            f"Data        : {self.data}\n"
            f"Prev Hash   : {self.previous_hash}\n"
            f"Hash        : {self.hash}\n"
        )


# ---------------------------
# Blockchain with PoS
# ---------------------------

class Blockchain:
    def __init__(self):
        self.chain = []
        self.validators = {}   # validator → stake
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, "Genesis Block", "0", "SYSTEM")
        self.chain.append(genesis)

    def add_validator(self, name, stake):
        self.validators[name] = stake

    # ---------------------------
    # Proof of Stake Selection
    # ---------------------------
    def select_validator(self):
        total_stake = sum(self.validators.values())
        pick = random.uniform(0, total_stake)

        current = 0
        for validator, stake in self.validators.items():
            current += stake
            if current > pick:
                return validator

    def add_block(self, data):
        validator = self.select_validator()
        previous_block = self.chain[-1]
        new_block = Block(
            len(self.chain),
            data,
            previous_block.hash,
            validator
        )
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(block)


# ---------------------------
# Run Example
# ---------------------------

if __name__ == "__main__":

    blockchain = Blockchain()

    # Add validators with stake
    blockchain.add_validator("Alice", 100)
    blockchain.add_validator("Bob", 50)
    blockchain.add_validator("Charlie", 150)

    # Add blocks
    blockchain.add_block("Transaction 1")
    blockchain.add_block("Transaction 2")
    blockchain.add_block("Transaction 3")

    blockchain.print_chain()