from helpers import alphabet_position, rotate_character
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenere(text, key):
    #Needs to iterate through key as well as text.
    final_code = ""
    m = len(key)
    vig_iterate = 0
    for i in text:
        if i.isalpha():
            key_position = alphabet_position(key[vig_iterate % m])
            final_code += rotate_character(i, key_position) #Why did changing key to key_position make a difference?
            vig_iterate += 1
        else:
            final_code += i
    return (final_code)
    

def main():
    message_to_encrypt = str(input("Please enter a message to be encrypted: "))
    key_to_encrypt = str(input("Please enter a keyword: "))
    final_message = vigenere(message_to_encrypt, key_to_encrypt)
    print(final_message)

if __name__ == "__main__":
    main()