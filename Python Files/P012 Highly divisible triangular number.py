#Highly divisible triangular number
import math

#Function to calculate triangular number
def triangular(n):
    sum = 0
    for i in range(n):
        sum += i+1
    return sum

num  = 76576500
while True:
    divisors = []
    num += 1
    for i in range(1,int(triangular(num)/2)+1):
        if (triangular(num) % i == 0):
            divisors.append(i)
    print(num, len(divisors))
    if (len(divisors) > 500):
        break

print(num, divisors)
