num = input ("ingrese numero: ")
num = int(num)
n=0
primo=range(2,10000)
lista= []
def main():
  global n,num,lista
  while num != 1:
    for prim in primo:
        if (num%prim)==0:
            elprimo=prim
            print elprimo
            num=num/prim
            break
main()