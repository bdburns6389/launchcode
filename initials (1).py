def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    initial_list = ''
    return [initial_list += (i[0].upper())   for i in name_list]
    # name_list = fullname.split()
    
    # for i in name_list:
    #     initial_list += (i[0].upper())
    # return(initial_list)


def main():
    print(get_initials(input("type a name: ")))
    # fullname = input("What is your full name?")
    # initials = (get_initials(fullname))
    # print(initials)
    # print("The initials of", fullname, "are", initials)

if __name__ == '__main__':
    main()