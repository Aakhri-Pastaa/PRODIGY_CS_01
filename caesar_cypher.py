
print("Welcome to Task 1 -> Caesar Cipher Encryption App. " +
      "This is a project 1 for Prodigy Infotech Cybersecurity Internship.")


UPPERCASE_START_CODE = ord("A")
UPPERCASE_END_CODE = ord("Z")
UPPERCASE_CHAR_RANGE = UPPERCASE_END_CODE - UPPERCASE_START_CODE + 1

def encrypt_with_caesar_cipher(message, shift_key):
    encrypted_message = ""
    for char in message.upper():
        if char.isalpha():
            char_code = ord(char)
            new_char_code = char_code + shift_key

            if new_char_code > UPPERCASE_END_CODE:
                new_char_code -= UPPERCASE_CHAR_RANGE

            if new_char_code < UPPERCASE_START_CODE:
                new_char_code += UPPERCASE_CHAR_RANGE

            new_char = chr(new_char_code)
            encrypted_message += new_char
        else:
            encrypted_message += char
    print(encrypted_message)


user_message = input("Message to Encrypt: ")
user_shift_key = int(input("Shift key to Encrypt (Integer): "))

encrypt_with_caesar_cipher(user_message, user_shift_key)

