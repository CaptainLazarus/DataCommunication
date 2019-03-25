def CheckLinear(n,k):
    pass

n = int(input("Enter n: "))
k = int(input("Enter k: "))
even = input("Is it even parity code? [y/n]\n")
if even == 'y':
    print(CheckLinear(n,k))
else:
    print("Not Linear")

#print(CheckLinear(n,k))