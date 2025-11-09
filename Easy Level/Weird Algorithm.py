n=int(input("Enter positive integer n."))
while n<1:
    print("n is a positive integer.")
    n=int(input("Enter positive integer n."))
while n!=1:
    print(n)
    if n%2==0:
        n=int(n/2)
    else:
        n=n*3+1
print(1)