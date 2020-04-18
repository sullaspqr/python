szam = "370" 
b=0
x = (int)(len(szam))
szorzat = []
for i in range(0,x,1):
    a=int(szam[i])
    szorzat.append(a*a*a)
for i in range(0,x,1):
    print(szorzat[i])
    b += int(szorzat[i])
armstrong = int(szam)
if (b==armstrong): 
    print(b, " = ", szam," tehát ez a szám Armstrong szám!")
elif(b<armstrong):
    print(b, "<", szam)
elif(b>armstrong):
    print(b,">", szam)