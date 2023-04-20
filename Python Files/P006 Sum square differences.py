#Sum square difference
sumOfSquares = 0
squareOfSum = 0
for i in range(100):
    sumOfSquares += i ** 2
    squareOfSum += i

squareOfSum ** 2

difference = squareOfSum - sumOfSquares
print(difference)
