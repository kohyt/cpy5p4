# q2_sum_series2.py

def sum_series2(i):
    if i == 1:
        return 1/3
    else:
        return (i/((2*i)+1)) + sum_series2(i-1)

# get input
i = int(input("Enter number:"))

# display results
print(sum_series2(i))
