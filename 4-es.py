szam = int(input("Kérek egy számot!"))
for i in range(1,szam *1+1, 1):
    print(("*"*(i*2-1)).center(szam*2-1," "))