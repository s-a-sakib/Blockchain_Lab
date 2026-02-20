import hashlib
import time


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            self.previous_hash +
            str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    # ---------------------------
    # Proof of Work Algorithm
    # ---------------------------
    def proof_of_work(self, difficulty):
        target = "0" * difficulty

        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

        return self.hash

    def __str__(self):
        return (
            f"\nBlock Index : {self.index}\n"
            f"Timestamp   : {self.timestamp}\n"
            f"Data        : {self.data}\n"
            f"Prev Hash   : {self.previous_hash}\n"
            f"Nonce       : {self.nonce}\n"
            f"Hash        : {self.hash}\n"
        )


class Blockchain:
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, "Genesis Block", "0")
        genesis.proof_of_work(self.difficulty)
        self.chain.append(genesis)

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        new_block.proof_of_work(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True


# ---------------------------
# Run Example
# ---------------------------

if __name__ == "__main__":

    blockchain = Blockchain(difficulty=4)

    blockchain.add_block("Alice sends 10 to Bob")
    blockchain.add_block("Bob sends 5 to Charlie")

    for block in blockchain.chain:
        print(block)

    print("Blockchain valid?", blockchain.is_chain_valid())

    # Save data to file
    with open("blockchain.txt", "w") as f:
        for block in blockchain.chain:
            f.write(str(block) + "\n")