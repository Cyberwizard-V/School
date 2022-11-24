import sys
import string

if __name__ == "__main__":
    try:
        x = input()
        reader = open(x)
    except FileNotFoundError:
        print(f"File {sys.argv , x} not found")
        quit()

    counts = dict()
    longestWords = []
    shortestWords = []
    for lists in reader.readlines():
        formatted = lists.translate(str.maketrans('', '', '@#%.')).replace("\n", "").split(" ")
        formatted2 = list(filter(None, formatted))
        #lower every word in formatted
        z = [x.lower() for x in formatted2]
        for word in z:
            if word in counts:
                counts[word.lower()] += 1
            else:
                counts[word.lower()] = 1

    for key, value in counts.items():
         if value == min(counts.values()):
             shortestWords.append(key)
         if value == max(counts.values()):
             longestWords.append(key)


    print(", ".join(longestWords))
    print(", ".join(shortestWords))