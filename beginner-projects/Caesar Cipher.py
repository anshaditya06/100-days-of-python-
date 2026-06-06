# Caesar Cipher
logo = """ 
   ██████╗  █████╗ ███████╗ █████╗ ██████╗ 
  ██╔════╝ ██╔══██╗██╔════╝██╔══██╗██╔══██╗
  ██║      ███████║█████╗  ███████║██████╔╝
  ██║      ██╔══██║██╔══╝  ██╔══██║██╔══██╗
  ╚██████╗ ██║  ██║███████╗██║  ██║██║  ██║
   ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

   ██████╗ ██╗██████╗ ██╗  ██╗███████╗██████╗
  ██╔════╝ ██║██╔══██╗██║  ██║██╔════╝██╔══██╗
  ██║      ██║██████╔╝███████║█████╗  ██████╔╝
  ██║      ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
  ╚██████╗ ██║██║     ██║  ██║███████╗██║  ██║
   ╚═════╝ ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""
print(logo)


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Global Variables
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encypting Function
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = (position + shift_amount) % 26 # Modulo to wrap around the alphabet / We can also use len(alphabets) instead of 26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")

# Decrypting Function
def decrypt(cipher_text, shift_amount):
      original_text = ""
      for letter in cipher_text:
            if letter in alphabets:
                  position = alphabets.index(letter)
                  new_position = (position - shift_amount) % len(alphabets) # Modulo to wrap around the alphabet / We can also use len(alphabets) instead of 26
                  original_text += alphabets[new_position]
            else:
                  original_text += letter
      print(f"The decoded text is {original_text}")

# Refactored Code to combine both encrypt and decrypt functions into one function with a direction parameter
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1 # To reverse the shift for decoding
    for letter in start_text:
        if letter not in alphabets:
            end_text += letter # If the letter is not in the alphabet, we just add it to the end_text without changing it
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = (position + shift_amount) % len(alphabets) # Modulo to wrap around the alphabet / We can also use len(alphabets) instead of 26
            end_text += alphabets[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")

caesar(text, shift, direction)

should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
while should_continue == "yes":
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      caesar(text, shift, direction)
      should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()