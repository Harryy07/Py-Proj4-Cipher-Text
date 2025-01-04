alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#User message : Harry #jctta
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for char in original_text:
        char_position_shifted= alphabet.index(char) + shift_amount # shift amount = 2 therefore 7 -> 9
        char_position_shifted %= len(alphabet) #will always keep between 0-25
        cipher_text += alphabet[char_position_shifted]

    print(f"Your encoded message is: {cipher_text} ")
encrypt(text, shift)

