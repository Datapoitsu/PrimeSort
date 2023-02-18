## -------------------- Primenumber finder -------------------- ##
#Written by: Aarni Junkkala

#Collects primes into a list and returns the prime of that index
primes = [2] #has two for bace, as it is easier to start from that
def CalculatePrimesIndex(i): #i = index
    global primes
   
    #If prime of the index isn't found, looks for it.
    if i > len(primes) - 1:
        num = primes[-1] + 1 #Starts from the one above last known prime
        
        while True:
            #Try to divide with every primenumber
            isPrime = True
            for k in range(len(primes)):
                #if answer is integer, then number isn't a prime
                if (num / primes[k]).is_integer() == True:
                    isPrime = False
                    break
            if isPrime == True:
                primes.append(num)
                #If enough primes have been calculated,
                #then will break and return the correct prime
                if i <= len(primes) - 1:
                    break
            num += 1
            
    return primes[i]

def CalculatePrimesNumber(n): #i = index
    global primes
   
    #If prime of the index isn't found, looks for it.
    if n > primes[len(primes) - 1]:
        num = primes[-1] + 1 #Starts from the one above last known prime
        
        while True:
            #Try to divide with every primenumber
            isPrime = True
            for k in range(len(primes)):
                #if answer is integer, then number isn't a prime
                if (num / primes[k]).is_integer() == True:
                    isPrime = False
                    break
            if isPrime == True:
                primes.append(num)
            #If enough numbers have been calculated,
            #then will break and return the correct prime
            if n <= num:
                break
            num += 1
            
    return primes[len(primes) - 1]

#Used for matematical usage, where prime1 = fisrt, where as in coding 0 is first.
def GetPrime(n):
    global primes
    if n - 1 > len(primes) - 1:
        CalculatePrimesIndex(n)
    return primes[n - 1]
    
if __name__ == '__main__':
    #Gets the prime that is 10th
    print(GetPrime(10))
    
    #Looks for a prime that is smaller than (n)
    print(CalculatePrimesNumber(50))
    
    #Gets the prime based on the index, this will return 101st 
    print(CalculatePrimesIndex(100))