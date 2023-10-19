import time
import matplotlib.pyplot as plt
import statistics
from utils import *

#
#
# PLOTTING GRAPH FOR GENERATING MULTIPLE 4 TO 32 BIT PRIME NUMBERS
#
#

s = int(input("input 's' parameter: "))
limit = int(input("num of prime numbers to generate: "))

times_naive = []
times_mr = []

avg_times_naive = []
avg_times_mr = []

for bin_len in range(4, 33):
    
    for i in range(10):
    
        bin_max = 2**(bin_len)-1
        bin_min = 2**(bin_len-1)

        p = random(bin_min, bin_max, lcg)

        
        start_time_mr = time.perf_counter()  # start tracking time
        miller_rabin_generate_multiple(p, s, limit, bin_max)
        end_time_mr = time.perf_counter()  # stop tracking time


        start_time_naive = time.perf_counter()  # start tracking time
        naive_generate_multiple(p, limit, bin_max)
        end_time_naive = time.perf_counter()  # stop tracking time

        # calculate elapsed time in ms
        elapsed_time_mr = round((end_time_mr - start_time_mr) * 1000, 2)
        times_mr.append(elapsed_time_mr)
        #print(f"\nelapsed time for Miller-Rabin (n = {bin_len}): {elapsed_time_mr}ms")

        elapsed_time_naive = round((end_time_naive - start_time_naive) * 1000, 2)
        times_naive.append(elapsed_time_naive)
        #print(f"elapsed time for naive (n = {bin_len}): {elapsed_time_naive}ms")
    
    # get average elapsed time for a smoother graph
    avg_times_naive.append(statistics.mean(times_naive))
    avg_times_mr.append(statistics.mean(times_mr))


# plot results
plt.plot(range(4, 33), avg_times_naive, label="naive")
plt.plot(range(4, 33), avg_times_mr, label="Miller-Rabin")

plt.xlabel("num of bits")
plt.ylabel("time (ms)")
plt.title("Generating 25 prime numbers")
plt.legend()

plt.show()



#
#
# PLOTTING GRAPH FOR DIFFERENT 's' PARAMETERS WHEN GENERATING A SINGLE 32-BIT PRIME NUMBER
#
#


bin_len = 32
times_mr = []
avg_times = []

for s in range(1, 21):
    for i in range(1000):

        bin_max = 2**(bin_len)-1
        bin_min = 2**(bin_len-1)

        p = random(bin_min, bin_max, lcg)

        start_time_mr = time.perf_counter()
        miller_rabin_generate(p, s)
        end_time_mr = time.perf_counter()

        # elapsed time in ms
        elapsed_time_mr = round((end_time_mr - start_time_mr) * 1000, 2)
        times_mr.append(elapsed_time_mr)
    
    avg_times.append(statistics.mean(times_mr))
    


plt.plot(range(1, 21), avg_times, label="Miller-Rabin")

plt.xlabel("parameter 's'")
plt.ylabel("time (ms)")
plt.title("Generating a single 32-bit prime number")

plt.show()