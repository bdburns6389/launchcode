def is_sorted(string):
    string_to_list = []
    for i in string:
        char_number = ord(i)
        string_to_list.append(char_number)
    
    final = sorted(string_to_list)
    
    test_list = ""
    for j in final:
        number_char = chr(j)
        test_list += number_char
        
    if test_list == string:
        return True
    else:
        return False
 
    
    
print(is_sorted("ABC"))
print(is_sorted("aBc"))
print(is_sorted("dog"))
