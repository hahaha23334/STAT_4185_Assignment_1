encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
def decrypt_transposition(message):
    chars = list(message)  # Convert the string to a list of characters
    length = len(chars)
    
    # Iterate through every second character
    for i in range(1, length, 2):
        # If the index from the beginning is >= the index from the end, stop
        if i >= length - i:
            break

        # Swap the characters
        chars[i], chars[length-i-1] = chars[length-i-1], chars[i]

    # Convert back to a string
    return ''.join(chars)

decrypted_message = decrypt_transposition(encrypted_message)
print(decrypted_message)
