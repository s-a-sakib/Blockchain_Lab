# Write a Python Program that Takes a String and the Desired Number of Leading Zeros from the 
# User and Outputs the Input String, the Nonce Value for Which the Leading Zeros Puzzle Is Solved, 
# and the Corresponding Hash Generated Using the SHA-256 Algorithm.

import hashlib as hash
string = input("Enter a string: ")
leading_zeros = int(input("Enter the desired number of leading zeros: "))
nonce = 0

while True:
    combined_string = string + str(nonce)
    hash_result = hash.sha256(combined_string.encode()).hexdigest()

    taget_zeros = '0' * leading_zeros

    if hash_result.startswith(taget_zeros):
        print(f"Input String: {string}")
        print(f"Nonce Value: {nonce}")
        print(f"Corresponding Hash: {hash_result}")
        break
    nonce += 1

