def encrypt_rail_fence(text, rails):
    """Encrypts the text using Rail Fence Cipher."""
    # Remove spaces from the text
    text = text.replace(" ", "")
    
    # Create empty rails
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1  # 1 for down, -1 for up

    # Build the zigzag pattern
    for char in text:
        fence[rail].append(char)
        rail += direction

        # Change direction at the top or bottom rail
        if rail == 0 or rail == rails - 1:
            direction = -direction

    # Read row by row for encryption
    encrypted = ''.join(''.join(row) for row in fence)
    return encrypted

def decrypt_rail_fence(cipher, rails):
    """Decrypts the Rail Fence Cipher text."""
    # Create empty rails
    fence = [[] for _ in range(rails)]
    rail_lengths = [0] * rails
    rail = 0
    direction = 1

    # Determine the length of each rail
    for _ in cipher:
        rail_lengths[rail] += 1
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction

    # Fill the rails with characters from the cipher
    index = 0
    for i in range(rails):
        for j in range(rail_lengths[i]):
            fence[i].append(cipher[index])
            index += 1

    # Read in zigzag order to decrypt
    rail = 0
    direction = 1
    decrypted = []
    for _ in cipher:
        decrypted.append(fence[rail].pop(0))
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction

    # Return the decrypted message
    return ''.join(decrypted)

if __name__ == "__main__":
    # Input from user
    text = input("Enter message to encrypt: ")
    rails = int(input("Enter key (number of rails): "))

    # Encryption
    encrypted_text = encrypt_rail_fence(text, rails)
    print(f"Encrypted message: {encrypted_text}")

    # Decryption
    decrypted_text = decrypt_rail_fence(encrypted_text, rails)
    print(f"Decrypted message: {decrypted_text}")
