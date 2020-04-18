msg = "ABCDFGKIKAA"
#print(msg)
#print (list(msg))
#print(sorted(set(msg)))
for karakter in set(msg):
print("{}:{}".format(karakter, msg.count(karakter)))