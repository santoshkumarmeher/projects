alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("Type 'encode' to encrypt ,Type 'decode' to decrypt: ")
text=input("Type your message: ").lower()
shift=int(input("Type the shift number: "))
if shift>=26:              #if user input the shift amount above 26
    shift=shift%26
def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position+shift_amount
        new_letter = alphabet[new_position]
        cipher_text+=new_letter
    print(f"the encoded text is : {cipher_text}")
def decrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position-shift_amount
        new_letter = alphabet[new_position]
        cipher_text+=new_letter
    print(f"the decoded text is : {cipher_text}")
if direction=="encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Please select correct option")

