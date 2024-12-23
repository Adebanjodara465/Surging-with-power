def powerOf4(number):
    count = 0
    #if only one set bit exists
    if (number & (~(number &(number - 1)))):

        while(number > 1):
            number >>= 1
            count += 1

    if (count % 2 == 0):
        return True
    else:
        return False    

print(powerOf4(4)  )