num = int(input("enter the number"))
print(num)
c = 1
for i in range (2,num):
    #print(i)
    if num % i == 0:
      c= 0
if c == 1:
    print("prime")
else:
    print("not prime")
