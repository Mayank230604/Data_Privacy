from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption

# Generate a key pair (private and public keys)
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

# Digitally sign the message
def sign_document(private_key, document: bytes) -> bytes:
    signature = private_key.sign(
        document,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256(),
    )
    return signature

# Verify the digital signature
def verify_signature(public_key, document: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(
            signature,
            document,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )
        return True
    except Exception:
        return False

if __name__ == "__main__":
    # User provides the document to sign
    document = input("Enter the content of the document to sign: ").encode()

    # Generate keys
    private_key, public_key = generate_keys()

    # Sign the document
    signature = sign_document(private_key, document)
    print("Document signed successfully.")

    # Verify the signature
    if verify_signature(public_key, document, signature):
        print("Signature is valid!")
    else:
        print("Signature is invalid!")
