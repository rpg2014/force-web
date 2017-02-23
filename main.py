from person import Person
import igraph
import csv
import numpy as np

reader = csv.reader('the_web.csv')

has_next = True
index = 0
people =[]
with open('the_web.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        people.append(row)


print people[0,:]
