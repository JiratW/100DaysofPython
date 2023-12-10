alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for char in text:
            index = alphabet.index(char) + shift
            if index > len(alphabet) - 1:
                index = index - len(alphabet)
            new_char = alphabet[index]
            cipher_text += new_char
        print(cipher_text)
    
    def decrypt(cipher_text, shift_amount):
        plain_text = ""
        for char in text:
            index = alphabet.index(char) - shift
            new_char = alphabet[index]
            plain_text += new_char
        print(plain_text)
    
    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(cipher_text=text, shift_amount=shift)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        print("Goodbye")
        should_continue = False
