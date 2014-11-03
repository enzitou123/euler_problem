__author__ = 'springfield'



n=range(0,100)
sum_n=0
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

for num in n:
    if F(num)>=4000000:
        break
    else:
        if F(num)%2==0:
            print F(num)
            sum_n=F(num)+sum_n
print sum_n