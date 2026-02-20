import hashlib
import time
class SimpleApplication:

    @staticmethod
    def sha256(data):
        return hashlib.sha256(data.encode()).hexdigest()

    def __init__(self):
        message1 = "Hello I am Sakib"
        message2 = "Hello i am Sakib"  # small change (I → i)

        print("Message 1:", message1)
        print("Hash 1   :", self.sha256(message1))

        print("\nMessage 2:", message2)
        print("Hash 2   :", self.sha256(message2))

class Block:
    def __init__(self, difficulty, data, previous_hash):
        self.timestamp = int(time.time())
        self.difficulty = difficulty
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
    
    def calculate_hash(self):
        block_str = (
            str(self.timestamp) + 
            self.data + self.previous_hash +
            str(self.nonce)
        )

        return hashlib.sha256(block_str.encode()).hexdigest()
    
    def mine(self):
        target = "0" * self.difficulty

        while True:
            hash_value = self.calculate_hash()
            if hash_value.startswith(target):
                print("Block mined!")
                break
            self.nonce += 1
        
    def print_block(self):
        print("\n==============================")
        print(f"Timestamp        : {self.timestamp}")
        print(f"Data             : {self.data}")
        print(f"Previous Hash    : {self.previous_hash}")
        print(f"Nonce            : {self.nonce}")
        print(f"Difficulty       : {self.difficulty}")
        print(f"Sha-256          : {self.calculate_hash()}")
        print("==============================\n")


if __name__ == "__main__":
    app = SimpleApplication()
    block = Block(4, "This is some block data", "0000000000000000")  # Example previous hash
    block.mine()
    block.print_block()