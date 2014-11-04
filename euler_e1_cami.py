def multipleSum():
    nSum=0
    counter=0
    for a in range(1000):
        if (a%3)==0 or (a%5) ==0:
            nSum+=a
            counter+=1
    print nSum


multipleSum()
