#make truth table with And and Or
def truthTable(op):
    #print first row
    print("A\tB\tA and B\tA or B")
    for a in [False, True]:
        for b in [False, True]:
            #print f string with the right format
            print(f"{a}\t{b}\t{eval(f'{a} {op} {b}')}")

truthTable("and")
print()
truthTable("or")

