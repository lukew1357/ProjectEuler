#Smallest multiple
found = False
target = 20 * 19
while found == False:
    target += 20
    if target % 19 == 0 and target % 18 == 0 and target % 17 == 0 and target % 16 == 0 and target % 15 == 0 and target % 14 == 0 and target % 13 == 0 and target % 12 == 0 and target % 11 == 0:
        found = True

print(target)
