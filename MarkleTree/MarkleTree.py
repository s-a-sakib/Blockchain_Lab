import hashlib


def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

def build_tree(transactions):
    # Current level of the tree (starting with leaf nodes)
    current_level = [sha256(tx) for tx in transactions]

    print("\n--- Leaf Hashes ---")
    for x in current_level:
        print(x)

    # Build the tree until we have only one hash (the root)
    while len(current_level) > 1:
        next_level = []

        if(len(current_level) % 2 != 0):
            current_level.append(current_level[-1])  # Duplicate last hash if odd number of nodes

        print("\n--- Next Level ---")

        for i in range(0, len(current_level), 2):
            combined_hash = current_level[i] + current_level[i + 1]
            new_hash = sha256(combined_hash)
            next_level.append(new_hash)
            print(new_hash)
        current_level = next_level
        
    return current_level[0]  # The root hash

def verify_transaction(transactions, root_hash):
    computed_root = build_tree(transactions)
    return computed_root == root_hash

if __name__ == "__main__":
    transactions = [
        "Alice pays Bob 5 BTC",
        "Bob pays Charlie 2 BTC",
        "Charlie pays Dave 1 BTC",
        "Dave pays Eve 0.5 BTC"
    ]

    print("\n==============================")
    print("Merkle Root:", build_tree(transactions))
    print("==============================")

    # Verify the transactions
    print("\nVerification:", verify_transaction(transactions, build_tree(transactions)))
    