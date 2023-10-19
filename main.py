import time
from utils import *


while True:
    try:
        print("\nSELECT OPTION:")
        print("1 ... TEST FOR PRIMALITY USING NAIVE TEST")
        print("2 ... TEST FOR PRIMALITY USING MILLER-RABIN TEST")
        print("3 ... GENERATE PRIME NUMBER USING NAIVE METHOD")
        print("4 ... GENERATE PRIME NUMBER USING MILLER-RABIN ALGORITHM")
        print("5 ... EXIT")
        selection = int(input("enter your selection: "))

        match selection:
            case 1:
                n = int(input("input number to check for primality: "))
                res = "prime" if naive_test(n) else "composite"
                print(f"{n} is a {res} number")
                
            case 2:
                n = int(input("input number to check for primality: "))
                s = int(input("enter 's' parameter for accuracy: "))
                res = "prime" if miller_rabin_test(n, s) else "composite"
                print(f"{n} is a {res} number")

            case 3:
                bin_len = int(input("input number of bits: "))
                bin_max = 2**(bin_len)-1
                bin_min = 2**(bin_len-1)

                print("[", bin_max, ",", bin_min, "]")

                p = random(bin_min, bin_max, lcg)
                print("generated: ", p)

                naive_generate(p)

            case 4:
                bin_len = int(input("input number of bits: "))
                bin_max = 2**(bin_len)-1
                bin_min = 2**(bin_len-1)

                print("[", bin_max, ",", bin_min, "]")

                p = random(bin_min, bin_max, lcg)
                print("generated: ", p)

                s = int(input("enter 's' parameter for accuracy: "))

                print("\nMiller-Rabin:")
                start_time = time.perf_counter()
                miller_rabin_generate(p, s)
                end_time = time.perf_counter()
                elapsed_time = (end_time - start_time) * 1000
                print(f"\nelapsed time for Miller-Rabin: {elapsed_time}ms")
            
            case 5:
                print("exiting...")
                break

            case _:
                print("wrong input")
    
    except ValueError:
        print("Invalid input, try again!")

