#Melyek a python nyelv fő jellemzői?
#Script , interpreted, oop, high-level, dynamically typed, general-purpose
#változók:
#my_int = 5
#my_float = 6.7
#my_boolean = True
#my_string = "Szöveg"
#my_semmi = None

#print(type(my_float))
#print(type(my_int))
#print(type(my_boolean))
#print(type(my_string))
#print(type(my_semmi))

#operátorok:
# = -> értékadás
#result = 3 + 7
#result = 10 - 5
#result = 5*10
#result = 10 / 5
#result = 10 // 7
#osztás utáni maradék:
#result = 11%3 # modulo

# hatványozás:
#result = 5 ** 3

first_number = 10
second_number = 20
third_number = 20

# kisebb, nagyobb, stb.
#result = first_number <= second_number

#nem azonosság:
#result = first_number != second_number
result = 125
#igaz vagy hamis elágazás:
#if (result % 2 == 0 and result > 100):
#    print("igaz")
# else:
# 
#     print("hamis")


# készítsünk elágazást, attól függően, hogy a második szám hogy viszonyul az elsőhöz
if (first_number > second_number):
    print("nagyobb")
elif (first_number < second_number):
    print("kisebb")
else:
    print("egyenlő")

# hogyan tudom a result változó értékét növelni hárommal?
result +=3

print(result)