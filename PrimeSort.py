## -------------------- Bogosort with primenumbers -------------------- ##
#Written by: Veeti "Thaumatized" Junkkala

import random
import sys
import PrimeNumbers

def Sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def Primesort(arr):
    PrimeIndex = 0
    while not Sorted(arr):
        changeIndex = PrimeNumbers.CalculatePrimesIndex(PrimeIndex) % len(arr)
        holder = arr[changeIndex]
        for i in range(changeIndex, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = holder
        PrimeIndex+=1

        
def RandArray(length = 10, maxvalue=255):
    arr = []
    for i in range(length):
        arr.append(random.randint(0, maxvalue))
    return arr
    
if __name__ == '__main__':
    length = 5
    maxvalue = 255
    arr = []

    #Args
    i = 1
    while i < len(sys.argv):
        '''Waiting for python3.10
            case "-l":
                length = int(sys.argv[i+1])
                i+=1
            case "-m":
                maxvalue = int(sys.argv[i+1])
                i+=1
            case "-a":
                while i+1 < len(sys.argv) and sys.argv[i+1].isnumeric():
                    arr.append(int(sys.argv[i+1]))
                    i+=1
        i+=1
        '''
        if sys.argv[i] == "-l":
            length = int(sys.argv[i+1])
            i+=1
        if sys.argv[i] == "-m":
            maxvalue = int(sys.argv[i+1])
            i+=1
        if sys.argv[i] == "-a":
            while i+1 < len(sys.argv) and sys.argv[i+1].isnumeric():
                arr.append(int(sys.argv[i+1]))
                i+=1
        i+=1
        
    
    #if empty generate random array and print it
    if arr == []:
        arr = RandArray(length, maxvalue)
        for number in arr:
            print(str(number) + ", ", end="")
        print()
    Primesort(arr)
    for number in arr:
        print(str(number) + ", ", end="")

