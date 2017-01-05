# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

csv_d = csv.DictReader(open("football.csv"))
fb_list = []
for i in csv_d:
    fb_list.append(i)


#convert dictionary values to int

for obj in fb_list:
    for key in obj:
        if key != 'Team':
            obj[key] = int(obj[key])

#create dictionary of teams and goal differentials
goal_diffs = {d['Team']: abs(d['Goals'] - d['Goals Allowed']) for d in fb_list}

#answer
ans = min(goal_diffs, key = goal_diffs.get)
print "The team with the smallest difference in goals is %s \nwith a total goal differential of %s goals." % (ans, goal_diffs[ans])
