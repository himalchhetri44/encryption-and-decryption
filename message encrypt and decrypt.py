"""
Simplified Vigenère Cipher Tool
A basic polyalphabetic cipher for encrypting and decrypting text using a key.
"""

class VigenereCipher:
    def __init__(self):
        # Alphabet: A-Z (26 letters)
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.size = 26

    def encrypt(self, text, key):
        """Encrypt text using the Vigenère cipher."""
        if not text or not key or not any(c.isalpha() for c in key):
            raise ValueError("Text and key must be non-empty, and key must have letters.")

        result = ""
        key = key.upper()
        key_index = 0

        for char in text:
            if char.isalpha():
                # Get indices for text and key letters (A=0, B=1, ..., Z=25)
                text_index = self.alphabet.index(char.upper())
                key_char = key[key_index % len(key)]
                key_index += 1
                key_index %= len(key)  # Cycle through key

                # Encrypt: Add indices, wrap around with modulo
                new_index = (text_index + self.alphabet.index(key_char)) % self.size
                new_char = self.alphabet[new_index]

                # Preserve original case
                result += new_char if char.isupper() else new_char.lower()
            else:
                # Keep non-letters unchanged
                result += char

        return result

    def decrypt(self, text, key):
        """Decrypt text using the Vigenère cipher."""
        if not text or not key or not any(c.isalpha() for c in key):
            raise ValueError("Text and key must be non-empty, and key must have letters.")

        result = ""
        key = key.upper()
        key_index = 0

        for char in text:
            if char.isalpha():
                # Get indices for text and key letters
                text_index = self.alphabet.index(char.upper())
                key_char = key[key_index % len(key)]
                key_index += 1
                key_index %= len(key)  # Cycle through key

                # Decrypt: Subtract indices, wrap around with modulo
                new_index = (text_index - self.alphabet.index(key_char)) % self.size
                new_char = self.alphabet[new_index]

                # Preserve original case
                result += new_char if char.isupper() else new_char.lower()
            else:
                # Keep non-letters unchanged
                result += char

        return result

def main():
    """Simple CLI for the Vigenère Cipher."""
    cipher = VigenereCipher()
    print("=== Vigenère Cipher Tool ===")
    
    while True:
        print("\n1. Encrypt\n2. Decrypt\n3. Exit")
        choice = input("Choose (1-3): ").strip()

        if choice == '3':
            print("Goodbye!")
            break
        if choice not in ['1', '2']:
            print("Invalid choice. Try 1, 2, or 3.")
            continue

        text = input("Enter text: ").strip()
        key = input("Enter key (must have letters): ").strip()

        try:
            if choice == '1':
                print("Encrypted:", cipher.encrypt(text, key))
            else:
                print("Decrypted:", cipher.decrypt(text, key))
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()