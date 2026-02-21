import hashlib as hash
import time

class Block:
    def __init__(self, data, previous_hash, difficulty):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = (
            str(self.timestamp) + 
            self.data + self.previous_hash+
            str(self.nonce)
        )
        return hash.sha256(hash_string.encode()).hexdigest()
    
    def __str__(self):
        return (
            f"\n--- Block ---\n"
            f"Timestamp     : {self.timestamp}\n"
            f"Data          : {self.data}\n"
            f"Previous Hash : {self.previous_hash}\n"
            f"Hash          : {self.hash}\n"
            f"Nonce         : {self.nonce}\n"
        )

    def mine_block(self):
        target = "0" * self.difficulty

        while True:
            temp_hash = self.calculate_hash()
            if temp_hash.startswith(target):
                self.hash = temp_hash
                break
            self.nonce = self.nonce + 1

class BlockChain:
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis = Block(
            "Genesis Block","0" * 64, self.difficulty
        )
        genesis.mine_block()
        self.chain.append(genesis)

    def add_block(self, data):
        self.previous_hash = self.chain[-1].hash
        new_block = Block(data, self.previous_hash, self.difficulty)
        new_block.mine_block()
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(block)
    
# ==========================
# MAIN
# ==========================
if __name__ == "__main__":
    blockchain = BlockChain(difficulty=4)

    blockchain.add_block("Alice pays Bob 10 BTC")
    blockchain.add_block("Bob pays Charlie 5 BTC")
    blockchain.add_block("Charlie pays Dave 2 BTC")

    blockchain.print_chain()