# Special Pythagorean triplet
for i in range(1000):
    for j in range(i):
        for k in range(j):
            if i + j + k == 1000 and k**2 + j**2 == i**2:
                print(k,'*',j,'*',i,'=',k*j*i)
                break
