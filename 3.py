#tuple ---------------------------------------------------
#tuple objektum:
my_tuple = (1,2,3)
my_tuple = (1,"cica",3)
#hozzunk létre egy új tuple-t és a régihez adjunk elemeket:
masodik_tuple = my_tuple + ("kutya", "birka")


#hányszor fordul elő a kutya elem:
eloford = masodik_tuple.count("kutya")
print(eloford)
#hanyadik indexen található a kutya?
eloford = masodik_tuple.index("kutya")

print(eloford)

#Dictionary -----------------------------------------------
# Kulcs (key) - Elem (value)
#készítsünk dictionary-t számozott szövegekkel:
my_dict = {1:"Hétfő", 2:"Kedd"}
#átírjuk a hétfőt monday-re:
my_dict[1] = "Monday"
#ha új kulcsot adok meg akkor az új elemet készít!
print(my_dict)

#Listaelem törlése:
#my_dict.pop(1)
del my_dict[2]
print(my_dict)