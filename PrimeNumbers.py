## -------------------- Primenumbers -------------------- ##
#Written by: Aarni Junkkala

import math

#Collects primes into a list and returns the prime of that index
primes = [2,3,5] #Has first 3 as it will help optimizing the code.

def CalculatePrimesIndex(n): #Returns the n:th prime
    global primes
    #If prime index is already found, returns that
    if n <= len(primes) - 1:
        return primes[n]
    
    num = primes[-1] #Starts from last known prime
    while True:
        num += 2 #Because primes are odd (except number 2), there is no point to check any odd numbers
        if str(num)[-1] == '5': #numbers ending with digit 5 aren't primes (except 5 it)
            num += 2

        #Prime can't be divisible with numbers higher that it's sqrt
        sqrt = int(math.sqrt(num))
                
        isPrime = True    
        for k in range(1,len(primes)): #Doesn't have to test number 2, because num can't be an even number
            if primes[k] > sqrt: #Limiter, so code doesn't test unnecessary numbers.
                break
            if num % primes[k] == 0: #If division goes perfectly onto number,
                isPrime = False #Then it isn't a prime
                break
        
        if isPrime == True: #It was a prime!
            primes.append(num)
            if n == len(primes) - 1: #If enough primes have been calculated,
                return primes[n] #then will break and return the correct prime

if __name__ == '__main__':
    # -- Testing the performance -- #
    import time
    Alku = time.time()
    dist = 5
    for i in range(1,dist):
        print(CalculatePrimesIndex(10 ** i))
    for i in range(dist,0,-1):
        print(CalculatePrimesIndex(10 ** i))
    print("Aika:" + str(time.time()-Alku))