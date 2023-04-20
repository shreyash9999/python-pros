alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' 'y', 'z','y']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt\n" )
text = input("Whats your message? \n"). lower()
shift = int(input("Number of shift \n"))
def encrypt (msg = text , num = shift):
    cyper_text = ""
    for letter in msg:
        position = alphabet.index(letter)
        new_position = position + num
        new_letter = alphabet[new_position]
        cyper_text += new_letter
    print(f"encrypt text is {cyper_text}")

def decrypt (msg2 = text , num2 = shift):
    cyper_text_2 = ""
    for letter in msg2:
        position = alphabet.index(letter)
        new_position = position - num2
        new_letter_2 = alphabet[new_position]
        cyper_text_2 += new_letter_2
    print(f"Decoded text is {cyper_text_2}")

if direction == "encrypt":
    encrypt()
elif direction == "decrypt":
    decrypt()