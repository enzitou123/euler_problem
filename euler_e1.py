__author__ = 'enzo'

natural=range(1,1000)
sum_n=0
print natural
for nat in natural:
    if nat%3==0 or nat%5==0:
        sum_n=sum_n+nat
print sum_n
