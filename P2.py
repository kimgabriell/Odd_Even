# kimgabriell

import os
import random

def main():

    while True:
        num=int(raw_input('Enter a number or type 0 to exit: '))
        if num== 0:
            print ("Thank You")
            break

        
        if int(num) % 2 == 0:
            print (format (num), 'is an Even number.')
        else:
            print (format (num), 'is an Odd number.')
            
main()

os.system ("pause")
