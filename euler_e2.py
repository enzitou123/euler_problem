__author__ = 'enzo'
import math
sum_n=0
def F1(n):
    return int(((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5)))




for num2 in range (2,100):
    if F1(num2)%2==0 and F1(num2)<=4000000:
        sum_n+=F1(num2)


print sum_n


#change the fibonacci rule so i don't have to apply the recursive function
#this one is the formula of Edouard Lucas changing the aureal number   /// aureal number = (1+sqrt(5))/2