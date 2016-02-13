# q7_find_largest.py

def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return max(alist[-1], find_largest(alist[:-1]))
    
# get input
##num = int(input("Enter number of integers:"))
##alist = []
##for i in range (num):
##    integer = input("Enter integer:")
##    alist.append(integer)
    
# display results
print(find_largest([5,1,8,7,2]))



