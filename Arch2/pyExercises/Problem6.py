"""
The Twelve Days of Christmas is a repetitive song that describes an increasingly long list of gifts sent to one’s true love on each of 12 days. 
A single gift is sent on the first day. A new gift is added to the collection on each additional day, and then the complete collection is sent. 
The first three verses of the song are shown below. The complete lyrics are available on the internet.

    On the first day of Christmas my true love sent to me: A partridge in a pear tree.

    On the second day of Christmas my true love sent to me: Two turtle doves, And a partridge in a pear tree.

    On the third day of Christmas my true love sent to me: Three French hens, Two turtle doves, And a partridge in a pear tree.


Your task is to write a program that displays the complete lyrics for The Twelve Days of Christmas. 
Write a function named "next_verse" that takes the verse number as its only parameter and displays the specified verse of the song. 
Then call that function 12 times with integers that increase from 1 to 12. Each item that is sent to the recipient in the song should only appear once in your program, 
with the possible exception of the partridge. It may appear twice if that helps you handle the difference between “A partridge in a pear tree” in the first verse and 
“And a partridge in a pear tree” in the subsequent verses.
"""

#Verse function
def next_verse(verse):
    #verse 1
    if verse == 1:
        print("On the first day of Christmas my true love sent to me: A partridge in a pear tree.")
    #verse 2
    elif verse == 2:
        print("On the second day of Christmas my true love sent to me: Two turtle doves, And a partridge in a pear tree.")
    #verse 3
    elif verse == 3:
        print("On the third day of Christmas my true love sent to me: Three French hens, Two turtle doves, And a partridge in a pear tree.")
    #verse 4
    elif verse == 4:
        print("On the fourth day of Christmas my true love sent to me: Four calling birds, Three French hens, Two turtle doves, And a partridge in a pear tree.")
    #verse 5
    elif verse == 5:
        print("On the fifth day of Christmas my true love sent to me: Five golden rings, Four calling birds, Three French hens, Two turtle doves, And a partridge in a pear tree.")
    #verse 6
    elif verse == 6:
        print("On the sixth day of Christmas my true love sent to me: Six geese a-laying, Five golden rings, Four calling birds, Three French hens, Two turtle doves, And a partridge in a pear tree.")
    #verse 7
    elif verse == 7:
        print("On the seventh day of Christmas my true love sent to me: Seven swans a-swimming, Six geese a-laying, Five golden rings, Four calling birds, Three French hens, Two turtle doves, And a partridge in a pear tree.")
    #verse 8
    elif verse == 8:
        print("On the eighth day of Christmas my true love sent to me: Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five golden rings, Four calling birds, Three French hens, Two turtle doves, And a partridge in a pear tree.")
    #verse 9
    elif verse == 9:
        print("On the ninth day of Christmas my true love sent to me: Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five golden rings, Four calling birds, Three French hens, Two turtle doves, And a partridge in a pear tree.")
    #verse 10
    elif verse == 10:
        print("On the tenth day of Christmas my true love sent to me: Ten lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five golden rings, Four calling birds, Three French hens, Two turtle doves, And a partridge in a pear tree.")
    #verse 11
    elif verse == 11:
        print("On the eleventh day of Christmas my true love sent to me: Eleven pipers piping, Ten lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five golden rings, Four calling birds, Three French hens, Two turtle doves, And a partridge in a pear tree.")
    #verse 12
    elif verse == 12:
        print("On the twelfth day of Christmas my true love sent to me: Twelve drummers drumming, Eleven pipers piping, Ten lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five golden rings, Four calling birds, Three French hens, Two turtle doves, And a partridge in a pear tree.")

def main():
    #iterate through the verses
    for i in range(1,13):
        #use verse function
        next_verse(i)

#call main
if __name__ == "__main__":
    main()
