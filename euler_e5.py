__author__ = 'enzo'
i = 3*5*2*7*11*13*17*19 #primes
while i%4!= 0 or i% 6!= 0 or i% 8!= 0 or i% 9!= 0 or i% 10!= 0 or i% 12!= 0 or i% 14!= 0 or i% 15!= 0 or i% 16!= 0 or i% 18!= 0 or i% 20!= 0:
  i+=3*5*2*7*11*13*17*19 #primes
print i

#this code is so slow! , i will change it when i have more knowledge of what im doing .it gets like 30sec, to give me the answer
#if have only the multipliers of the primes its like really fast one and i dont have to have so much OR statements