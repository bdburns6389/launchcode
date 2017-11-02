def get_country_codes(prices):
    lst = []
    prices_list = prices.split(", ")
    for items in prices_list:
        k = items.split("$") #splits each list item by $
        z = (k[0])  #gets first two letters in "k" list.
        lst.append(z)
    return ", ".join(lst)  #Can make work in string but not list
    
print (get_country_codes("DK$300, JK$240, CA$400"))


