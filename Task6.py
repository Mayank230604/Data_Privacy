import itertools
import string

def bruteforce_attack(password, char_set):
    attempts = 0
    for length in range(1, len(password) + 1):
        for guess in itertools.product(char_set, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return (attempts, guess)
    return (attempts, None)

password = input("Input the password to crack: ")
char_set = string.digits  # Restrict to digits
attempts, guess = bruteforce_attack(password, char_set)
if guess:
    print(f"Password cracked in {attempts} attempts. The password is {guess}.")
else:
    print(f"Password not cracked after {attempts} attempts.")
