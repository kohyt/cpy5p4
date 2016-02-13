# q5_count_letter.py

def count_letter(string,ch):
    if len(string) == 1 and string == ch:
        return 1
    elif len(string) == 1 and string != ch:
        return 0
    else:
        if string[-1] == ch:
            return 1 + count_letter(string[:-1],ch)
        else:
            return count_letter(string[:-1],ch)

# get input
string = input("Enter word/phrase:")
ch = input("Enter letter:")

# display results
print(count_letter(string,ch))


