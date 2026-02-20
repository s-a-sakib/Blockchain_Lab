import hashlib as hash
input_string = str(input("Enter a string to hash: "))
difficulty = int(input("Enter the difficulty level (number of leading zeros): "))

nonce = 0
difficulty_prefix = '0' * difficulty

while True:
    combined_string = input_string + str(nonce)

    hash_result = hash.sha256(combined_string.encode()).hexdigest()
    if hash_result.startswith(difficulty_prefix):
        print(f"Nonce found: {nonce}")
        print(f"Hash: {hash_result}")
        break
    nonce += 1
