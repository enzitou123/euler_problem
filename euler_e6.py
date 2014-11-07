__author__ = 'enzo'
def Diff ():
    SumAll=0
    SumSqrt_Max=0
    for SumSqrt in range(1,101):
        SumAll+=SumSqrt
        SumSqrt_Max+=(SumSqrt)**2


    print (SumAll)**2-SumSqrt_Max

Diff()