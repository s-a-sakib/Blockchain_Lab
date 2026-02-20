import hashlib as hash
import time
import json

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __repr__(self):
        return f"Transaction (sender={self.sender}, receiver={self.receiver}, amount={self.amount})"

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [str(tx) for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hash.sha256(block_string).hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        tx = Transaction("Genesis", "Alice", 10000)
        genesis_block = Block(0, [tx], "0")
        self.chain.append(genesis_block)

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for tx in block.transactions:
                if tx.receiver == address:
                    balance += tx.amount
                elif tx.sender == address:
                    balance -= tx.amount
        return balance

    def add_block(self, transactions):
        previous_hash = self.chain[-1].hash
        approved_transactions = []
        for tx in transactions:
            if self.get_balance(tx.sender) < tx.amount:
                print(f"Transaction from {tx.sender} to {tx.receiver} for {tx.amount} failed: insufficient balance.")
                return False
            approved_transactions.append(tx)
        new_block = Block(len(self.chain), approved_transactions, previous_hash)
        self.chain.append(new_block)
        return True

    def get_utxo(self, address):
        utxos = []
        for block in self.chain:
            for tx in block.transactions:
                if tx.receiver == address:
                    utxos.append(tx)
                elif tx.sender == address:
                    utxos = [utxo for utxo in utxos if utxo != tx]
        return utxos

if __name__ == "__main__":
    blockchain = BlockChain()
    print("Initial Balance of Alice:", blockchain.get_balance("Alice"))
    
    tx1 = Transaction("Alice", "Bob", 2000)
    tx2 = Transaction("Alice", "Charlie", 3000)
    
    blockchain.add_block([tx1, tx2])
    
    print("Balance of Alice after transactions:", blockchain.get_balance("Alice"))
    print("Balance of Bob:", blockchain.get_balance("Bob"))
    print("Balance of Charlie:", blockchain.get_balance("Charlie"))
    
    print("\nUTXOs for Alice:", blockchain.get_utxo("Alice"))
    print("UTXOs for Bob:", blockchain.get_utxo("Bob"))
    print("UTXOs for Charlie:", blockchain.get_utxo("Charlie"))
