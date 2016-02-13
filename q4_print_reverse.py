# q4_print_reverse.py

def reverse_int(n):
    if n == "":
        return n
    else:
        return n[-1] + reverse_int(n[:-1])

# get input
n = input("Enter integer:")

# display results
print(reverse_int(n))


