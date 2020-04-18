str1, str2 = "Ungváli", "Péter"

name = str1 +" "+ str2
name += " ma sajnos nincs jelen"

first_letter = name[0]
last_letter = name[-1]
last_letter = name[len(name)-1]
print(first_letter)
print(last_letter)

modified = name.replace("l","r")

# összes szó új sorba:
szavak = name.split(" ")

for word in szavak:
    print(word)   
else:               # akkor fut le, ha a for ciklus gond nélkül lefutott!
        print("Random")

lista = [1,2,3]
#hanyadik elem a sajnos a szavak-ban:
index = szavak.index("sajnos")
print(szavak)
print(index)

#vegyük ki az első két elermet és tegyük egy új listába:
uj_lista = szavak[:2]
print(uj_lista)

#szúrjuk be a egy számot a 10. után:
my_list = [1,2,3,4,5,6,7,8,9,10]
my_list.insert(len(my_list),11)
print(my_list)

#Módosítsuk a második elemet -2-re:
my_list[1] = -2
print(my_list)
#eltávolítjuk a -2 elemet:
my_list.remove(-2)

#adott elem szerepel-e a listában?
if (-2 not in my_list):
    print("nincs benne a -2")

#vegyük ki a negyedik indexű elem után minden másodikat
my_list = [1,2,3,4,5,6,7,8,9,10]
uj_list = my_list[3::2]
print(uj_list)

#írjunk egy loop-ot ami addig kér be számot, amíg az > nem lesz mint 10
number =0
while number < 10:
    number = int(input())
