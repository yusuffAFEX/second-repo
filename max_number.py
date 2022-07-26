# def max_number(number_list):
#     max_num = 0
#
#     for num in number_list:
#         if num > max_num:
#             max_num = num
#     return max_num
#
# print(max_number([45,89,23,10]))


def max_number(number_list):
    l = list(number_list)
    l.sort()
    return l[-1]
print(max_number([45,89,23,10]))

def grid(num):
    i=0
    while i<num:
        print('-'*num)
        print('|'*num)
        i +=1
grid(5)