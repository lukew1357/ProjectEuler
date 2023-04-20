#Largest palindrome product
product = ""
reverse = []
answer = []
array = []
found = False

while found == False:
    for i in range(0, 1000):
        for j in range (0, 1000):
            ii = 1000 - i
            jj = 1000 - j
            product = int(ii * jj)
            productLen = len(str(product))
            for k in range(productLen):
                array.append(product[productLen - k])
            print(array)
            
            reverse = product.reverse()
            print(product, reverse)
            if product == reverse:
                answer.append(ii, jj, product)
                found = True

print(answer)
            
        
