__author__ = 'enzo'
#really difficult one :( , im thinking about it
primeNum=0
for num in range(2,10000000):
    if all(num%i!=0 for i in range(2,num)):
       primeNum+=1
       if primeNum==10001:
           print num
           break