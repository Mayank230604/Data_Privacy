import random

def generate_password():
    # Open dictionary file
    with open('dictionary.txt') as f:
        words = f.read().splitlines()
    
    # Randomly select four words
    password = random.sample(words, 2)
    
    # Combine words with hyphens
    password = '-'.join(password)
    
    return password

# Example usage
password = generate_password()
print(f"Generated Password: {password}")
