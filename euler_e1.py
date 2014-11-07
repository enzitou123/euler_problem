__author__ = 'enzo'
def multipleSum(n):
    nSum=0
    for a in range(n-1,0,-1):
        if (a%3)==0 or (a%5) ==0:
            nSum+=a
    print nSum
multipleSum(1000)