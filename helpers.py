import string
#use ascii lower and upper instead of making list for alpahbet.
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_position(letter):
    if letter in alphabet:
        return(alphabet.index(letter))
    elif letter in alphabet_cap:
        return(alphabet_cap.index(letter))

def rotate_character(char, rot):
    if char in alphabet:
        a = alphabet_position(char)
        a = (a + rot) % 26
        a = (alphabet[a])
    elif char in alphabet_cap:
        a = alphabet_position(char)
        a = (a + rot) % 26
        a = (alphabet_cap[a])
    return(a)