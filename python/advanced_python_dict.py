'''Q6'''

import csv, re

fac = csv.reader(open("faculty.csv"))

last_only = lambda x: re.split(r' ', x)[-1]

faculty_list = [[last_only(i[0]), i] for i in fac]

same_name = []

for i, value in enumerate(faculty_list):
    last_name = faculty_list[i][0]
    if i == 0:
        same_name.append(value)
        print i, value
    elif last_name == same_name[len(same_name) - 1][0]:
        same_name[len(same_name) -1].append(faculty_list[i][1])
        print i, value
    else:
        same_name.append(value)
        print i, value

faculty_dict = {i[0]: i[1:] for i in same_name}

first_few = {key: faculty_dict[key] for key in faculty_dict.keys()[0:3]}
print first_few

'''Q7'''

import csv, re

fac = csv.reader(open("faculty.csv"))

def name_tup(full_name):
    name_split = re.split(r' ', full_name)
    first, last = name_split[0], name_split[-1]
    return (first, last)

professor_dict = {name_tup(name[0]): name[1:] for name in fac}

first_profs = {key: professor_dict[key] for key in professor_dict.keys()[0:3]}
print first_profs

'''Q8'''

names = [key for key in professor_dict]
names.sort(key = lambda x: x[1])

for key in names:
    print key, professor_dict[key]
