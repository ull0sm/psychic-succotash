def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


N = int(input("How many numbers of the Fibonacci series would you like to generate? : "))
if(N>0):
    print("your series is:")
    for i in range(N):
        print(f"{fibo(i)}",end="\t")    
else:
    print("wrong entry.....")
    