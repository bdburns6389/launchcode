def sort_contacts(contacts):
    newList=[]
    for key, value in sorted(contacts.items()):
        new_tuple = (key, *value)
        newList.append(new_tuple)
    print (newList)


sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
        "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
        "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")})
