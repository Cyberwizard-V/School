import sys
import os


def main():
    textFile = input()
    try:
        if textFile.find(',') > 1:
            x = textFile.split(',')
            cleanUpX = [x.strip(' ') for x in x]
            print(cleanUpX)
            for i in cleanUpX:
                if os.path.exists(i.strip()) is False:
                    print("File cannot be found, please check the name")
                    return
                with open(i) as f:
                    lines = f.readlines()
                for x in lines:
                    if "def" in x and "#" not in lines[lines.index(x) - 1]:
                        print(
                            f"File: {i} contains a function [{x[4:].replace(':', '')}] on line [{lines.index(x) + 1}] without a preceding comment. ")
        else:
            with open(textFile) as f:
                lines = f.read().splitlines()
            for i in lines:
                if "def" in i and "#" not in lines[lines.index(i) - 1]:
                    print(
                        f"File: {textFile} contains a function [{i[4:].replace(':', '')}] on line [{lines.index(i) + 1}] without a preceding comment. ")
    except BaseException:
        print("File cannot be found, please check the name")
        return

    for thing in sys.argv:
        print(thing, end='  ')


if __name__ == '__main__':
    main()
