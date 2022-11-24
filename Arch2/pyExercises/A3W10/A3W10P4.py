# Write a program that displays the word (or words) that occur most and least frequently in a file.
# Your program should begin by reading the name of the file from the user. Then it should find the word(s)
# by splitting each line in the file at each space. Finally, any leading or trailing punctuation marks should be
# removed from each word. In addition, your program should ignore capitalization.
# As a result, apple, apple!, Apple and ApPlE sh
import sys
import os


def main():
    textFile = input()

    # check if the file exist
    if os.path.exists(textFile.strip()) is False:
        print("File cannot be found, please check the name")
        return

    with open(textFile) as f:
        lines = f.read().splitlines()

    for thing in sys.argv:
        print(thing, end='  ')

    myList = []
    for i in lines:
        x = i.split()
        myList.append(x)

    # add all lists together
    myList = [item for sublist in myList for item in sublist]

    # Filter all special characters and make every word lower case
    removeChar = str.maketrans('', '', '@#%.')
    out_list = [s.translate(removeChar) for s in myList]
    z = [x.lower() for x in out_list]

    zFrequent = [(z.count(x), x) for x in set(z)]
    max_count = max(zFrequent)[0]
    cleaned = []
    for i in zFrequent:
        if i[0] == max_count:
            cleaned.append(i[1])

    def getAllindex(lst, elem):
        return list(filter(lambda a: lst[a] == elem, range(0, len(lst))))

    zCount = [z.count(xx) for xx in z]
    LeastFreq = getAllindex(zCount, min(zCount))
    MostFreq = getAllindex(zCount, max(zCount))
    lL = list(set([z[ii] for ii in LeastFreq]))
    lM = list(set([z[ii] for ii in MostFreq]))

    lL.sort(reverse=True)
    print(lL, lM)


if __name__ == '__main__':
    main()
