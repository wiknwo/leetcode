# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# Decomposition of M into maximal odd decomposition

def solution(N):
    # write your code in Python 3.6
    max_odd_decomp_of_n = []
    # Handling special cases first
    if N == 2:
        return max_odd_decomp_of_n
    elif N == 1 or N == 3 or N == 5 or N == 7:
        max_odd_decomp_of_n.append(N)
        return max_odd_decomp_of_n
    else:
        runningsum, count, i = 0, 0, 1
        # Loop through and compute odd number divisors
        while (runningsum + i) < N:
            max_odd_decomp_of_n.append(i)
            count += 1
            runningsum += i
            i += 2
        start, r = 0, N - runningsum
        if r % 2 == 0:
            max_odd_decomp_of_n[count - 1] += r
        elif r > max_odd_decomp_of_n[count - 1]:
            max_odd_decomp_of_n.append(r)
            count += 1
        else:
            start = 1
            max_odd_decomp_of_n[count - 1] += r + 1
        return max_odd_decomp_of_n
    


    
    
