Primesort is a successor to bogosort. It has been improved by using primes to shuffle the array, instead of actual random numbers. This makes it consistent with the same array, and only increases the compute time by a ton!

Starting array is printed only if -a is not used.  

Command line arguments:
	-l length, how long of a list is used. default 10.  
	-m max, biggest number allowed in the list. default 255.  
	-a values..., values used to specify an array to sort. overrides -c and -v.

Example commands:
	python PrimeSort.py -a 7 3 2 9 5
	python PrimeSort.py -l 7 -m 100
