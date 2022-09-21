#FIBOWACCKIE SEQUENCE ??????
x = int(input("Enter a number: "))

#Get fibonacci sequence from x
def fib(x):
    # hard code 0 1
    a, b = 0, 1
    #While loop zolang a kleiner is dan x. 
    while a < x:
        print(a)
        #fibonacci sequence berekening en we willen 0 en 1 hebben ^ . a , b is dan b , a en dat moet dan + b   
        a , b = b , a + b

fib(x)


