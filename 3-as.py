i=1
for i in range(101):
    # for i in range (0,10,2) - kettessével lépeget
    # for i in range(0,-10,-2)
    if ((i%3 ==0) and (i%7==0)):
         print("PiffPuff")
    elif(i%3==0):
        print("Piff")
    elif(i%7==0):
        print("Puff")
    else:
            print(i)

