import string


def alphabet_position(letter):
    if letter in string.ascii_lowercase:
        return(string.ascii_lowercase.index(letter))
    elif letter in string.ascii_uppercase:
        return(string.ascii_uppercase.index(letter))

def rotate_character(char, rot):
    if char in string.ascii_lowercase:
        a = alphabet_position(char)
        a = (a + rot) % 26
        a = (string.ascii_lowercase[a])
    elif char in string.ascii_uppercase:
        a = alphabet_position(char)
        a = (a + rot) % 26
        a = (string.ascii_uppercase[a])
    return(a)

def encrypt(text, rot):
    message = ""
    for i in text:
        if i.isalpha():
            message += rotate_character(i, rot)
        else:
            message += i
    return message
    
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
    
print(vigenere("The crow flies at midnight!", "boom"))
#Uvs osck rmwse bh auebwsih!

