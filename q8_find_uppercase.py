# q8_find_uppercase.py

def find_num_uppercase(string):
    if len(string)== 1:
        if string[-1].isupper():
            return 1
        else:
            return 0
    else:
        if string[-1].isupper():
            return 1 + find_num_uppercase(string[:-1])
        else:
            return find_num_uppercase(string[:-1])

# get input
string = input("Enter word/phrase:")

# display results
print(find_num_uppercase(string))


