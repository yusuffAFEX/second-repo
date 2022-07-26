def case_count(word:str):
    t = []
    r = []
    for i in word:
        if i.isupper():
            t.append(i)
        if i.islower():
            r.append(i)
    return f'{len(t)} is number of uppercase and {len(r)} is number of lowercase.'





print(case_count('Wwg'))



