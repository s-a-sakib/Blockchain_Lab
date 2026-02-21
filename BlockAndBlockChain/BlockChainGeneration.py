from Block import Block

class BlockChain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(
            version="1.0",
            previous_hash="0" * 64,
            merkle_root="dummy_merkle_root",
            difficulty=self.difficulty
        )
        genesis_block.mine_block()   
        self.chain.append(genesis_block)

    def add_block(self, merkle_root="dummy_merkle_root"):
        previous_hash = self.chain[-1].hash
        new_block = Block(
            version="1.0",
            previous_hash=previous_hash,
            merkle_root=merkle_root,
            difficulty=self.difficulty
        )
        new_block.mine_block()   
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


if __name__ == "__main__":
    blockchain = BlockChain(difficulty=3)

    # Add 5 blocks
    for i in range(5):
        blockchain.add_block()
        print(f"Block {i+1} added: {blockchain.chain[-1]}")

    print("\nBlockchain valid:", blockchain.is_chain_valid())