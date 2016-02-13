# q1_sum_series1.py

def sum_series1(i):
    if i == 1:
        return 1
    else:
        return (1/i) + sum_series1(i-1)

# get input
i = int(input("Enter number:"))

# display results
print(sum_series1(i))

