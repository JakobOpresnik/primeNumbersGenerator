import math


# linear congruential generator (LCG)
def LCG(m, a, b, r0):
    r1 = r0

    while True:
        r1 = (a*r1 + b) % m
        yield r1

# generates a random number on [a, b] interval using LCG
def random(a, b, lcg):
    return a + int(next(lcg) % (b-a+1))

# used so that a**b doesn't exceed number of bits
def modular_exponentiation(a, b, n):
    result = 1
    a %= n  # ensure a is within modulus range

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        a = (a * a) % n
        b //= 2

    return result


# super-duper LCG seed
lcg = LCG(2**32, 69069, 0, 1)

# checks if a number is prime or not
# False - certainly a composite number
# True - probably a prime number (not necessarily)
def miller_rabin_test(p, s):
    if p <= 3:
        return True
    if p % 2 == 0:
        return False
    
    d = p - 1
    k = 0
    while d % 2 == 0:
        d = d // 2
        k += 1
    
    for _ in range(s):
        a = random(2, p-2, lcg)
        #x = pow(a, d, p)  # regular exponentiation
        x = modular_exponentiation(a, d, p)
        if x == 1:
            continue

        for _ in range(k-1):
            if x == p - 1:
                break
            #x = pow(x, 2, p)
            x = modular_exponentiation(x, 2, p)
        
        if x != p-1:
            return False
    
    return True

# generates a prime number using the Miller-Rabin test
def miller_rabin_generate(p, s):
    while miller_rabin_test(p, s) == False:
        p += 2
        print(p, "is a composite number")
    print(p, "is a prime number")

# generates multiple prime numbers using the Miller-Rabin test
def miller_rabin_generate_multiple(p, s, l, bin_max):
    limit = l
    i = 0
    while p <= bin_max:
        if miller_rabin_test(p, s) == True:
            #print(p)
            p += 2
            i += 1
            if i >= limit:
                return
        else:
            p += 2
            
# naively checks if a number is prime or not
def naive_test(p):
    if p <= 3:
        return True
    if p % 2 == 0:
        return False
    
    while True:
        j = 3
        while j <= math.sqrt(p):
            if p % j == 0:
                break
            j += 2
        if j > math.sqrt(p):
            return True
        return False

# naively generates a prime number
def naive_generate(p):
    if p % 2 == 0:
        p += 1
    
    while True:
        j = 3
        while j <= math.sqrt(p):
            if p % j == 0:
                break
            j += 2
        if j > math.sqrt(p):
            print(p)
            return
        
        p += 2

# naively generates multiple prime numbers
def naive_generate_multiple(p, l, bin_max):
    limit = l
    i = 0
    if p % 2 == 0:
        p += 1
    
    while p <= bin_max:
        j = 3
        while j <= math.sqrt(p):
            if p % j == 0:
                break
            j += 2
        if j > math.sqrt(p):
            #print(p)
            i += 1
            if i >= limit:
                return
        
        p += 2