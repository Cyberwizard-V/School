import time
import keyboard
from termcolor import cprint

# fun way to shutdown your pc 
# countdown in seconds 10 seconds
def count():
    for i in range(10, 0, -1):
        cprint(str(i) + " seconds remaining.", 'green', attrs=['bold'])
        time.sleep(1)


# fullscreen please :)
def fullscreen():
    keyboard.press('f11')

def main():
    time.sleep(1)
    fullscreen()
    count()
        
main()