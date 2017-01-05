import csv
import re

# read faculty.csv into python as list
fac = csv.reader(open("faculty.csv"))

'''Q1'''

#extract degree column from faculty list
fac_ls = [i[1] for i in fac]

# convert list into string type
fac_ls = ','.join(text)

#remove . from string
fac_ls = re.sub(r'\.', '', fac_ls)

#list of distinct Degrees in list (set(fac_ls))
degs = ['MD', 'MPH', 'PhD', 'ScD', 'BS', '0', 'MS', 'JD']

#create dictionary for distinct values and their counts
deg_count = {x: len(re.findall(x, fac_ls)) for x in degs}
print deg_count

'''Q2'''

#extract titles column from csv and store is list
titles = [i[2] for i in fac]

#strip leading and trailing white space and convert to string
titles = [str(x).strip() for x in titles]

#result of set(titles) shows distinct titles
set(titles)
(['Assistant Professor of Biostatistics', 'Professor of Biostatistics', 'Associate Professor of Biostatistics', 'Assistant Professor is Biostatistics', 'title'])

#create function to search for Strings 'Professor', 'Assistant', and 'Associate' title list
def title_count(title):
    title_match = [re.match(r'^' + title, i) for i in titles]
    return len([i.group(0) for i in title_match if i is not None])

#Create Dictionary of Title and their counts
ranks = ['Professor', 'Assistant', 'Associate']

answer = {i: title_count(i) for i in ranks}
print answer

'''Q3'''

#create list of emailes with list compression
emails = [i[3] for i in fac]

#remove header
emails.remove(' email')

print emails

'''Q4'''

#create list of all domains based off emails
domains = [re.split(r'@', i)[1] for i in emails]

#find unique domains
set(domains)
