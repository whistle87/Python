n = int(input("Enter width: "))
m = int(input("Enter length: "))
k = int(input("Enter a number of slices: "))
if k % n == 0 or k % m == 0:
    print("yes")
else:
    print("no")
