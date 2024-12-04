import hashlib

def hash_password(password: str) -> str:
    """Hashes a password using SHA-256."""
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

if __name__ == "__main__":
    password = input("Enter a password to hash: ")
    hashed_password = hash_password(password)
    print(f"SHA-256 Hash: {hashed_password}")
