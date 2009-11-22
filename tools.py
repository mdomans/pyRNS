"""
some code for use with Residual Number System, may be usefull if you like to play with some cryptography

"""


import operator

def vector_boundary(vector):
    return reduce(operator.mul, primes_vector)
        
def to_RNS(number, vector):
    if not vector:
        assert isinstance(primes_vector, (list, tuple))
        if number>vector_boundary(vector):
            raise TypeError, 'to small vector chosen'
    return [number%elem for elem in vector]
    
def generate_vector(system_limit):
    numbers = range(3, system_limit, 2)
    mroot = system_limit ** 0.5
    half = len(numbers)
    i = 0
    m = 3
    while m <= mroot:
        if numbers[i]:
          j = (m * m - 3)//2
          numbers[j] = 0
          while j < half:
            numbers[j] = 0
            j += m
        i = i + 1
        m = 2 * i + 3
    return [2]+[x for x in numbers if x]