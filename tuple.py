#take tup1 one variable 
tup1=(1,"DEEPAK",2.45874456,True ,False,10+4j,"kalyan","pooja")
#print the tup1 value
print(tup1)
#for get lenght and type ,negative and positive accessing we use below 
print(tup1[1])
print(tup1[-3])
print(type(tup1))
print(len(tup1))
print(tup1[2:4])
print("DEEPAK" in  tup1)
print("kalyan" not in tup1)
print("pooja" in tup1)
for items in tup1:
    print("one by one print items in tup1:",items)