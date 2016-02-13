# q3_find_gcd.py

def gcd(m,n):
    if m % n == 0:
        return n
    else:
        return gcd(n,m % n)

# get input
m = int(input("Enter 1st number:"))
n = int(input("Enter 2nd number:"))

# display results
print(gcd(m,n))

def testrun():
    if gcd(24,16) == 8 or gcd(255,25) == 5:
        return True
    else:
        return False

    
