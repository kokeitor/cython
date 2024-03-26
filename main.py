from Paquetes.optimization import execution_time

import time

import Paquetes.utils

import sys

import cython

sys.setrecursionlimit(10000)  # Ajustar el límite de profundidad de la recursión




@Paquetes.utils.memorize

def calculate_primes_optimized(amount):

    primes = []

    number  = 2

    found  = 0

    while found < amount:

        for x in primes:

            if number % x == 0:

                break

        else:

            primes.append(number)

            found += 1

        number += 1

    return primes

 

def calculate_primes(amount):

    primes = []

    number  = 2

    found  = 0

    while found < amount:

        for x in primes:

            if number % x == 0:

                break

        else:

            primes.append(number)

            found += 1

        number += 1

    return primes

 

@cython.boundscheck(True)

@cython.cdivision(True)

@cython.wraparound(True)

@cython.nonecheck(True)

def calculate_primes_c_wrapped(int amount):

   

    cdef int number

    cdef int found

    cdef int x

   

    cdef int primes[100000]

   

    amount = min(amount,100000)

    number  = 2

    found = 0

   

    while found < amount:

        for x in primes[:found]:

            if number % x == 0:

                break

        else:

            primes[found] = (number)

            found += 1

        number += 1

       

    return [p for p in primes[:found]]

 

def calculate_primes_c(int amount):

   

    cdef int number

    cdef int found

    cdef int x

   

    cdef int primes[100000]

   

    amount = min(amount,100000)

    number  = 2

    found = 0

   

    while found < amount:

        for x in primes[:found]:

            if number % x == 0:

                break

        else:

            primes[found] = (number)

            found += 1

        number += 1

       

    return [p for p in primes[:found]]




@cython.boundscheck(True)

@cython.cdivision(True)

@cython.wraparound(True)

@cython.nonecheck(True)

cpdef calculate_primes_c_static_wrapped(int amount):

   

    cdef int number

    cdef int found

    cdef int x

   

    cdef int primes[100000]

   

    amount = min(amount,100000)

    number  = 2

    found = 0

   

    while found < amount:

        for x in primes[:found]:

            if number % x == 0:

                break

        else:

            primes[found] = (number)

            found += 1

        number += 1

       

    return [p for p in primes[:found]]




cpdef calculate_primes_c_static(int amount):

   

    cdef int number

    cdef int found

    cdef int x

   

    cdef int primes[100000]

   

    amount = min(amount,100000)

    number  = 2

    found = 0

   

    while found < amount:

        for x in primes[:found]:

            if number % x == 0:

                break

        else:

            primes[found] = (number)

            found += 1

        number += 1

       

    return [p for p in primes[:found]]





def fibonacci_recursive_c(int n):

    if n < 2:

        return n

    return fibonacci_recursive_c(n-1) +  fibonacci_recursive_c(n - 2)

 

def fibonacci_recursive(n):

    if n < 2:

        return n

    return fibonacci_recursive(n-1) +  fibonacci_recursive(n - 2)




cpdef fibonacci_recursive_c_st(n):

    if n < 2:

        return n

    return fibonacci_recursive_c_st(n-1) +  fibonacci_recursive_c_st(n - 2)





@cython.boundscheck(True)

@cython.cdivision(True)

@cython.wraparound(True)

@cython.nonecheck(True)

def fibonacci_recursive_c_wrapped(int n):

    if n < 2:

        return n

    return fibonacci_recursive_c_wrapped(n-1) +  fibonacci_recursive_c_wrapped(n - 2)

 

@cython.boundscheck(True)

@cython.cdivision(True)

@cython.wraparound(True)

@cython.nonecheck(True)

cpdef fibonacci_recursive_c_st_wrapped(int n):

    if n < 2:

        return n

    return fibonacci_recursive_c_wrapped(n-1) +  fibonacci_recursive_c_wrapped(n - 2)