import main_c #from main_c_static import calculate_primes_c

import time




if __name__ == '__main__':

   

    """

    start_execution = time.time()

    main_c.calculate_primes(100000)

    end_execution = time.time()

    print(end_execution-start_execution)

   

    start_execution = time.time()

    main_c.calculate_primes_c(100000)

    end_execution = time.time()

    print(end_execution-start_execution)

 

    start_execution = time.time()

    main_c.calculate_primes_c_wrapped(100000)

    end_execution = time.time()

    print(end_execution-start_execution)

   

    start_execution = time.time()

    main_c.calculate_primes_c_static(100000)

    end_execution = time.time()

    print(end_execution-start_execution)

   

   

    start_execution = time.time()

    main_c.calculate_primes_c_static_wrapped(100000)

    end_execution = time.time()

    print(end_execution-start_execution)

    """

   

    #-------

   

   

    start_execution = time.time()

    main_c.fibonacci_recursive(100)

    end_execution = time.time()

    print(end_execution-start_execution)

   

    start_execution = time.time()

    main_c.fibonacci_recursive_c(100)

    end_execution = time.time()

    print(end_execution-start_execution)

   

    start_execution = time.time()

    main_c.fibonacci_recursive_c_st(100)

    end_execution = time.time()

    print(end_execution-start_execution)

   

    start_execution = time.time()

    main_c.fibonacci_recursive_c_wrapped(100)

    end_execution = time.time()

    print(end_execution-start_execution)

   

   

    start_execution = time.time()

    main_c.fibonacci_recursive_c_st_wrapped(100)

    end_execution = time.time()

    print(end_execution-start_execution)

 