__author__ = 'springfield'
import math
primeNum=1
for num in range(1,2000000,2):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       primeNum+=num
print primeNum