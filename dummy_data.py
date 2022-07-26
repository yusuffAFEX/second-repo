dummy_data = [

    {'firstname': 'Yusuff',
     'lastname': 'Oyedele',
     'date of birth': '11-11-1999',
     'attendance': 11,
     'height': '1.7m',
     'weight': '50kg',
     'age': '22'},

    {'firstname': 'Awwal',
     'lastname': 'Adeleke',
     'date of birth': '01-10-1976',
     'attendance': 10,
     'height': '1.5m',
     'weight': '60kg',
     'age': '43'},

    {'firstname': 'Abraham',
     'lastname': 'Adekunle',
     'date of birth': '21-11-1996',
     'attendance': 9,
     'height': '1.8m',
     'weight': '65kg',
     'age': '25'},

    {'firstname': 'Abdulwali',
     'lastname': 'Tajudeen',
     'date of birth': '15-01-1990',
     'attendance': 8,
     'height': '1.4m',
     'weight': '40kg',
     'age': '29'},

    {'firstname': 'Adebusola',
     'lastname': 'Adeyeye',
     'date of birth': '12-11-1996',
     'attendance': 9,
     'height': '1.6m',
     'weight': '55kg',
     'age': '25'},

    {'firstname': 'Basheer',
     'lastname': 'Balogun',
     'date of birth': '11-11-1980',
     'attendance': 7,
     'height': '1.7m',
     'weight': '50kg',
     'age': '40'},

    {'firstname': 'Abdullahi',
     'lastname': 'Salaam',
     'date of birth': '02-07-1994',
     'attendance': 11,
     'height': '1.55m',
     'weight': '53kg',
     'age': '27'},

    {'firstname': 'Faith',
     'lastname': 'Adeosun',
     'date of birth': '11-02-1995',
     'attendance': 5,
     'height': '1.51m',
     'weight': '49kg',
     'age': '26'},

    {'firstname': 'ahmad',
     'lastname': 'sharafudeen',
     'date of birth': '11-10-1993',
     'attendance': 10,
     'height': '1.5m',
     'weight': '50kg',
     'age': '28'},

    {'firstname': 'Lukman',
     'lastname': 'Abisoye',
     'date of birth': '11-11-1998',
     'attendance': 11,
     'height': '1.65m',
     'weight': '56kg',
     'age': '24'},

    {'firstname': 'toluwanimi',
     'lastname': 'Ogunbiyi',
     'date of birth': '07-11-1960',
     'attendance': 11,
     'height': '1.73m',
     'weight': '50kg',
     'age': '57'},

]


def attendance_increment(firstname: str):
    for i in dummy_data:
        if i['firstname']==firstname:
            i['attendance'] += 1
    return dummy_data

print(attendance_increment('toluwanimi'))


# def update_profile(firstname, new_firstname, new_lastname):
#     for i in dummy_data:
#         if i['firstname']==firstname:
#             i['firstname'] = new_firstname
#             i['lastname'] = new_lastname
#     return dummy_data
#
# print(update_profile('ahmad', 'deniyi', 'sharaf'))


def full_names():
    all_names = []
    for i in dummy_data:
        all_names.append(i['firstname'] + ' ' + i['lastname'])
        # all_names.append(i['lastname'])
    return all_names


print(full_names())


# def add_new_profile(firstname, lastname, date_of_birth, attendance: int, height, weight, age):
#     dic = {
#         'firstname': firstname,
#         'lastname': lastname,
#         'date of birth': date_of_birth,
#         'attendance': attendance,
#         'height': height,
#         'weight': weight,
#         'age': age,
#     }
#     dummy_data.append(dic)
#     return dummy_data
#
# print(add_new_profile('oyedele', 'lawal', '1-2-2000', 5, '1.2m', '54kg', '19'))


# def number_of_student():
#     return len(dummy_data)
#
# print(number_of_student())
#
# def remove_profile(firstname):
#     for i in dummy_data:
#         if i['firstname'] == firstname:
#             dummy_data.remove(i)
#     return dummy_data
#
# print(remove_profile('Awwal'))

def birth_month(firstname):
    for i in dummy_data:
        if i['firstname'] == firstname:
            t = i['date of birth'].split('-')
    if int(t[1]) == 1:
        return 'January'
    elif int(t[1]) == 2:
        return 'February'
    elif int(t[1]) == 3:
        return 'March'
    elif int(t[1]) == 4:
        return 'April'
    elif int(t[1]) == 5:
        return 'May'
    elif int(t[1]) == 6:
        return 'June'
    elif int(t[1]) == 7:
        return 'July'
    elif int(t[1]) == 8:
        return 'August'
    elif int(t[1]) == 9:
        return 'September'
    elif int(t[1]) == 10:
        return 'October'
    elif int(t[1]) == 11:
        return 'November'
    elif int(t[1]) == 12:
        return 'December'


print(birth_month('Faith'))


def group_profile_by_month(month):
    l = []
    for i in dummy_data:
        t = i['date of birth'].split('-')
        if int(t[1]) == month:
            l.append(i)
    return l


print(group_profile_by_month(10))


def list_of_initial():
    initials = []
    for i in dummy_data:
        initials.append(i['firstname'][0] + ' ' + i['lastname'][0])
    return initials


print(list_of_initial())


def bmi_calculator(firstname):
    for i in dummy_data:
        if i['firstname'] == firstname:
            s = i['height'].strip('m')
            s1 = i['weight'].strip('kg')
            bmi = int(s1) / (float(s) * float(s))
    return bmi


print(bmi_calculator('Awwal'))


def minimum_age():
    l = []
    for i in dummy_data:
        s = int(i['age'])
        l.append(s)
        l.sort()
    return l[0]


print(minimum_age())


def maximum_age():
    l = []
    for i in dummy_data:
        s = int(i['age'])
        l.append(s)
        l.sort()
    return l[-1]


print(maximum_age())


def average_age():
    l = []
    for i in dummy_data:
        s = int(i['age'])
        l.append(s)
    return sum(l) / 2


print(average_age())


def birth_year(firstname):
    for i in dummy_data:
        if i['firstname'] == firstname:
            t = i['date of birth'].split('-')
    return t[2]


print(birth_year("Awwal"))
