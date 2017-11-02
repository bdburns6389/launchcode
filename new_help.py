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