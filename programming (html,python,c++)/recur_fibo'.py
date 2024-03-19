def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    

while True:
    nterms = int(input("How many terms: "))
    if nterms <=0:
        print("Please enter a postive number: ") 
    else:
        print("Fibonacci sequence: ")
        for i in range(nterms):
            print(recur_fibo(i), end=", ")
             