from helpers import alphabet_position, rotate_character
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(text, rot):
    message = ""
    for i in text:
        if i.isalpha():
            message += rotate_character(i, rot)
        else:
            message += i
    return message
    
def main():
    message_to_encrypt = str(input("Type a message: "))
    key_to_encrypt = str(input("Rotate by: "))
    final_message = encrypt(message_to_encrypt, key_to_encrypt)
    print(final_message)
    
if __name__ == "__main__":
    main()
    


