#Even Fibonacci numbers
fib1 = 1
fib2 = 2
fibC = 0
while fib1 <= 4000000:
    if fib1 % 2 == 0:
        fibC += fib1
    fib1, fib2 = fib2, fib1 + fib2

print(fibC)
