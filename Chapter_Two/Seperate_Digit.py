num = int(input("Enter five digit number: "))
A = num // 10000 
B = num // 1000 % 10
C = num // 100 % 10
D = num // 10 % 10
E = num % 10
print(A,"\t",B,"\t",C,"\t",D,"\t",E)

if num > 5:
    print("invalid input")
