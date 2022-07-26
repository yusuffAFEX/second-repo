import string


def decode(data: str):
    digits = string.digits
    # s_chars = string.punctuation
    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    rev_alpha_lower = alpha_lower[::-1]
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_map = ['#', '$', '%', '@', '*']
    dec = list()
    input_str = list(data)

    var_len = len(input_str)
    i = 0
    while i < var_len:
        if input_str[i] in vowels_map:
            dec.append(vowels[vowels_map.index(input_str[i])])
        elif input_str[i] == '^':
            dec.append(digits[rev_alpha_lower.index(input_str[i + 1])])
            input_str.pop(i + 1)
            var_len -= 1
        elif input_str[i] in alpha_upper + alpha_lower:
            dec.append(input_str[i].swapcase())
        elif input_str[i] == '|':
            dec.append(input_str[i + 1])
            input_str.pop(i + 1)
            var_len -= 1

        i += 1

    return ''.join(dec)


# print(decode('#D$@L#'))
print(decode('gf|^|#|^|#gd|*|#hsjBBDGHFY$HSH^w^t^v^rDNDH'))
#GF^#^#GD*#HSJbbdghfyehsh3648dndh
