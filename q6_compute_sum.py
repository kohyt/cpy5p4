# q6_compute_sum.py

def sum_digits(n):
    if n // 10 == 0:
        return n
    else:
        return (n % 10) + sum_digits(n//10)

# get input
n = int(input("Enter integer:"))

# display results
print(sum_digits(n))
