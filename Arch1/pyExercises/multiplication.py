#make multiplication table that shows all combinations of 1-10
def multTable():
    # them cute numbers
    print("x\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10")
    #for x in range 1 - 11 cuz we want all combinations? DUHHH sorry for my sucky comments
    for x in range(1,11):
        #format text the right way so we which number is which with f string
        print(f"{x}\t{x*1}\t{x*2}\t{x*3}\t{x*4}\t{x*5}\t{x*6}\t{x*7}\t{x*8}\t{x*9}\t{x*10}")

        
multTable()
