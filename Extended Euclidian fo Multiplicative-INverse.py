print("Plese Enter Values Greater then zero")
r1 = int(input("Enter Value of r1 : "))
r2 = int(input("Enter Value of r2 : "))
t1 = 0
t2 = 1
temp_r1 = r1
temp_r2 = r2

while(r2 > 0):
    q = (int)(r1 / r2)
    r = r1 - (q * r2)
    t = t1 - (q * t2)
    t1 = t2
    t2 = t
    r1 = r2
    r2 = r

if(r2 == 0):
    print("multiplicative inverse of", temp_r2, " is ", t2 + t1 + temp_r1)

else:
    print("Please Enter Correct Values!")


