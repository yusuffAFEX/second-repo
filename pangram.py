import string

def pangram(w: str):
    letters = string.ascii_lowercase
    l = list(w)
    for letter in letters:
        if letter not in l:
            return False
    return True



print(pangram("two driven jocks help fax my big quiz"))