import hashlib


# Function to calculate SHA-256 hash
def sha256_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


# 1️⃣ Deterministic Property
def test_deterministic():
    print("\n--- Deterministic Test ---")
    data = "Hello Blockchain"
    hash1 = sha256_hash(data)
    hash2 = sha256_hash(data)

    print("Hash 1:", hash1)
    print("Hash 2:", hash2)
    print("Deterministic:", hash1 == hash2)


# 2️⃣ Fixed Length Property
def test_fixed_length():
    print("\n--- Fixed Length Test ---")
    data1 = "Hi"
    data2 = "This is a very long input string to test hash length"

    hash1 = sha256_hash(data1)
    hash2 = sha256_hash(data2)

    print("Length of Hash 1:", len(hash1))
    print("Length of Hash 2:", len(hash2))
    print("Fixed Length:", len(hash1) == len(hash2))


# 3️⃣ Avalanche Effect
def test_avalanche():
    print("\n--- Avalanche Effect Test ---")
    data1 = "Hello"
    data2 = "Hella"  # Slight change

    hash1 = sha256_hash(data1)
    hash2 = sha256_hash(data2)

    print("Original Hash :", hash1)
    print("Modified Hash :", hash2)


# 4️⃣ Simple Collision Check
def test_collision():
    print("\n--- Collision Test (Simple Demo) ---")
    seen_hashes = {}
    
    for i in range(10000):
        data = f"data_{i}"
        h = sha256_hash(data)
        
        if h in seen_hashes:
            print("Collision found!")
            return
        
        seen_hashes[h] = data

    print("No collision found in 10,000 attempts.")


if __name__ == "__main__":
    test_deterministic()
    test_fixed_length()
    test_avalanche()
    test_collision()