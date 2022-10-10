"""
If you have 3 straws, possibly of differing lengths, it may or may not be possible to lay them down so that they form a triangle when their ends are touching. 
For example, if all of the straws have a length of 6 inches. then one can easily construct an equilateral triangle using them. However, 
if one straw is 6 inches. long, while the other two are each only 2 inches. long, then a triangle cannot be formed. 
In general, if any one length is greater than or equal to the sum of the other two then the lengths cannot be used to form a triangle. 
Otherwise they can form a triangle. Write a function called "check_triangle" that determines whether or not three lengths can form a triangle. 
The function will take 3 parameters and return a Boolean result. 
In addition, write a program that reads 3 lengths from the user and demonstrates the behaviour of this function, on a correct triangle print possible otherwise impossible.
"""
def check_triangle(a, b, c):
    #triangle check
    if a >= b + c or b >= a + c or c >= a + b:
        #false
        return(False)
    else:
        #true
        return(True)

def main():
    #Inputs
    a = float(input("Enter the first length: "))
    b = float(input("Enter the second length: "))
    c = float(input("Enter the third length: "))
    #check the triangle if true
    if check_triangle(a, b, c) == True:
        print("Possible")
    else:
        print("Impossible")

if __name__ == "__main__":
    main()

