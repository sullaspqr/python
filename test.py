#készítsünk egy metódust, ami ki tudja nyomntatni egy változó típusát

def tipust_nyomtat(variable):
    print(type(variable))
tipust_nyomtat(1)

#készítsünk egy metódust, ami visszaadja a leghosszabb szót
def return_longest_word(sentence):
    words = sentence.split(" ") # lista
    longest_word = ""

    for elem in words:
        if (len(elem)< len(longest_word)): 
            longest_word = elem

    return longest_word

print(return_longest_word("Ez egy különösen hosszú mondat"))