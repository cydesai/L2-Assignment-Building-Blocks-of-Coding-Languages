def vigenere_encrypt(plaintext, key):
    # Convert the plaintext and key to uppercase
    plaintext = plaintext.upper()
    key = key.upper()

    ciphertext = []
    key_index = 0
    key_length = len(key)

    for char in plaintext:
        if char.isalpha():  # Encrypt only alphabetic characters
            # Calculate the shift using the key
            shift = ord(key[key_index % key_length]) - ord('A')
            #print(shift)
            # Encrypt the character
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext.append(encrypted_char)
            # Move to the next character in the key
            key_index += 1
        else:
            # Non-alphabetic characters are added as is
            ciphertext.append(char)

    return ''.join(ciphertext)


plaintext = 'HELLO WORLD'
key = 'KEY'
ciphertext = vigenere_encrypt(plaintext, key)
print(ciphertext)
