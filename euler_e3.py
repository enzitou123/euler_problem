__author__= "enzo"
def prime_number():
  n=600851475143
  while n != 1:
    for primNum in range (2,10000):
        if (n%primNum)==0:
            primMax=primNum
            n=n/primNum
            break
  print primMax

prime_number()


#change the variables names