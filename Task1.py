def encrypt_caesar(text, shift):
    """Encrypts the text using Caesar Cipher."""
    encrypted = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char  # Non-alphabetic characters are unchanged
    return encrypted

def decrypt_caesar(cipher, shift):
    """Decrypts the Caesar Cipher text."""
    return encrypt_caesar(cipher, -shift)  # Decrypt by reversing the shift

if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted_text = encrypt_caesar(text, shift)
    print(f"Encrypted Text: {encrypted_text}")
    
    decrypted_text = decrypt_caesar(encrypted_text, shift)
    print(f"Decrypted Text: {decrypted_text}")
