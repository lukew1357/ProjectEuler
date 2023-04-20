#Largest prime factor
import math

factors = [600851475143]

#Function to check if a number is prime
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i == 0):
            return False
    return True

#Loops through factors of the target value and appends if factor is prime
while True:
    if (isPrime(factors[0])):
        break
    for i in range(2, int(factors[0])):
        if (factors[0] % i == 0):
            factors[0] = factors[0] / i
            factors.append(i)
            break

#Sorts factors and prints last factor in the list
factors.sort()
print(factors[len(factors)-1])




