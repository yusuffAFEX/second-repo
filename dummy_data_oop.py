class Profile():
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

    def __int__(self):
        pass


    def get_user(self, firstname):
        for i in self.dummy_data:
            if i['firstname'] == firstname:
                self.firstname = i['firstname']
                self.lastname = i['lastname']
                self.dob = i['date of birth']
                self.attendance = i['attendance']
                self.height = i['height']
                self.weight = i['weight']
                self.age = i['age']
                return
        return f'No profile for {firstname}'

    def attendance_increment(self):
        if hasattr(self, 'attendance'):
           self.attendance += 1
        else:
            print('Profile has no attribute')
        # for i in self.dummy_data:
        #     if i['firstname'] == self.firstname:
        #         i['attendance'] += 1
        #         break
        # return i

    def update_profile(self, new_firstname, new_lastname):
        for i in self.dummy_data:
            if i['firstname'] == self.firstname:
                i['firstname'] = new_firstname
                i['lastname'] = new_lastname
                break
        return self.dummy_data

    def list_of_full_names(self):
        all_names = []
        for i in self.dummy_data:
            all_names.append(i['firstname'] + ' ' + i['lastname'])
            # all_names.append(i['lastname'])
        return all_names

    def add_new_profile(self, firstname, lastname, date_of_birth, attendance: int, height, weight, age):
        dic = {
            'firstname': firstname,
            'lastname': lastname,
            'date of birth': date_of_birth,
            'attendance': attendance,
            'height': height,
            'weight': weight,
            'age': age,
        }
        return self.dummy_data.append(dic)

    def number_of_student(self):
        return self.dummy_data.count()

    def remove_profile(self):
        for i in self.dummy_data:
            if i['firstname'] == self.firstname:
                self.dummy_data.remove(i)
                break
        return self.dummy_data

    def birth_month(self):
        months = {1: 'January', 2: 'February', 3: 'March', 4: "May"}
        for i in self.dummy_data:
            if i['firstname'] == self.firstname:
                t = i['date of birth'].split('-')[1]
                profile_month = months[t]
                break

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

    def group_profile_by_month_of_birth(self, month: int):
        l = []
        for i in self.dummy_data:
            t = i['date of birth'].split('-')
            if int(t[1]) == month:
                l.append(i)
        return l

    def list_of_initial(self):
        initials = []
        for i in self.dummy_data:
            initials.append(i['firstname'][0] + ' ' + i['lastname'][0])
        return initials

    def bmi_calculator(self):
        for i in self.dummy_data:
            if i['firstname'] == self.firstname:
                s = i['height'].strip('m')
                s1 = i['weight'].strip('kg')
                bmi = int(s1) / (float(s) * float(s))
                break
        return bmi

    def minimum_age(self):
        l = []
        for i in self.dummy_data:
            s = int(i['age'])
            l.append(s)
            l.sort()
            break
        return l[0]

    def maximum_age(self):
        l = []
        for i in self.dummy_data:
            s = int(i['age'])
            l.append(s)
            l.sort()
        return l[-1]

    @classmethod
    def average_age(cls):
        l = []
        for i in cls.dummy_data:
            s = int(i['age'])
            l.append(s)
        return sum(l) / 2

    def birth_year(self):
        for i in self.dummy_data:
            if i['firstname'] == self.firstname:
                t = i['date of birth'].split('-')
                break
        return t[2]



profile = Profile()
profile.get_user("yusuff")
profile.attendance_increment()
print(profile.attendance)
