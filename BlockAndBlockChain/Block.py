import hashlib as hash
import time
class Block:

        
    def __str__(self):
        return (
            f"\n--- Block ---\n"
            f"Version       : {self.version}\n"
            f"Previous Hash : {self.previous_hash}\n"
            f"Merkle Root   : {self.merkle_root}\n"
            f"Timestamp     : {self.timestamp}\n"
            f"Nonce         : {self.nonce}\n"
            f"Hash          : {self.hash}\n"
        )
    
    def __init__(self, version, previous_hash, merkle_root, difficulty):
        self.version = version
        self.previous_hash = previous_hash
        self.merkle_root = merkle_root
        self.timestamp = int(time.time())
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = None
    
    def calculate_hash(self):
        block_string = (
            str(self.version) +
            self.previous_hash +
            self.merkle_root +
            str(self.timestamp) +
            str(self.nonce)
        )
        return hash.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        target = '0' * self.difficulty
        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith(target):
                break
            self.nonce += 1
        return self.hash
    
    def verify_block(self):
        return self.hash == self.calculate_hash()
    


# # Example usage
# if __name__ == "__main__":
#     block = Block(
#         version="1.0",
#         previous_hash="0" * 64,
#         merkle_root="dummy_merkle_root",
#         difficulty=4
#     )
#     print("Mining block...")
#     mined_hash = block.mine_block()
#     print(f"Block mined: {mined_hash}")
#     print(block)
#     print(f"Block valid: {block.verify_block()}")