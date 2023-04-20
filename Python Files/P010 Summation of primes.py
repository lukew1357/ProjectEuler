#Summation of primes
import math
sumPrimes =  0

#Function to check if a number is prime
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i == 0):
            return False
    return True

#Loops from 2 (1 is not a prime) to 2 million summing the prime numbers
for i in range(2,2000000):
    if isPrime(i):
        sumPrimes += i
        
print(sumPrimes)
