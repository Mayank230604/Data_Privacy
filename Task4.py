import hashlib
import requests

# Function to check if a password has been pwned using the Have I Been Pwned API
def check_password_leak(password: str) -> bool:
    """Checks if the password has been leaked using the Have I Been Pwned API."""
    # Generate SHA-1 hash of the password
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    
    # Make the API request to check the leaked passwords
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    
    if response.status_code != 200:
        raise RuntimeError("Error fetching data from API")
    
    # Split the response and check if the password suffix exists in the API response
    hashes = (line.split(":") for line in response.text.splitlines())
    return any(suffix == h for h, _ in hashes)

# Function to read usernames and passwords from a file and check each password
def check_passwords_from_file(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into username and password
            username, password = line.strip().split(',')
            try:
                # Check if the password is leaked
                if check_password_leak(password):
                    print(f"[LEAKED] {username}'s password '{password}' has been leaked!")
                else:
                    print(f"[SAFE] {username}'s password '{password}' is safe.")
            except RuntimeError as e:
                print(f"Error checking password for {username}: {e}")

if __name__ == "__main__":
    # Input the file path containing usernames and passwords
    file_path = input("Enter the file path containing usernames and passwords: ")
    check_passwords_from_file(file_path)
