
def caesar_decrypt(key, message):
    """Decrypt a message using a given key"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_message = []
    
    for char in message:
        if char.isalpha():
            if char.islower():
                shifted_index = (alphabet.index(char) - key) % 26
                decrypted_message.append(alphabet[shifted_index])
            elif char.isupper():
                shifted_index = (alphabet.index(char.lower()) - key) % 26
                decrypted_message.append(alphabet[shifted_index].upper())
        else:
            decrypted_message.append(char)
    return ''.join(decrypted_message)

def process_file(filename): 
    """Read, sort and return a file""" 
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            items = [word.strip() for word in lines if word.strip()]
            sorted_items = sorted(items)
            return filename, sorted_items, len(lines)
    except Exception as e:
        print(f"Error processing file: {e}")
        return None, [], 0

def crack_caesar_cipher(encrypted_message, common_words):
    """Attempt to crack the Caesar cipher by trying all possible keys"""
    for key in range(1, 26):
        decrypted_message = caesar_decrypt(key, encrypted_message)
        words = decrypted_message.split()
        matches = sum(1 for word in words if word.lower() in common_words)
        if matches > 0:
            print(f"Key: {key} -> {decrypted_message} (Matches: {matches})")

# Process the common words file
filename, common_words_list, _ = process_file("common_words.txt")

# Convert the common words list to a set for fast lookup
common_words_set = set(common_words_list)

# Crack the Caesar Cipher
encrypted_message = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"
crack_caesar_cipher(encrypted_message, common_words_set)
