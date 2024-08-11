def caesar_encrypt(key, message):
    """Encrypt a message using Caesar cipher with the given key."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    encrypted_message = ""
    
    for char in message:
        if char.isupper():
            encrypted_message += shifted_alphabet[alphabet.index(char)]
        elif char.islower():
            encrypted_message += shifted_alphabet[alphabet.index(char.upper())].lower()
        else:
            encrypted_message += char
    
    return encrypted_message

def caesar_decrypt(key, message):
    """Decrypt a message using Caesar cipher with the given key."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    decrypted_message = ""
    
    for char in message:
        if char.isupper():
            decrypted_message += alphabet[shifted_alphabet.index(char)]
        elif char.islower():
            decrypted_message += alphabet[shifted_alphabet.index(char.upper())].lower()
        else:
            decrypted_message += char
    
    return decrypted_message

plaintext = "Experience is the teacher of all things."
key = 12

encrypted_message = caesar_encrypt(key, plaintext)
print("Encrypted message:", encrypted_message)

decrypted_message = caesar_decrypt(key, encrypted_message)
print("Decrypted message:", decrypted_message)
