from person import Person
from igraph import *
import csv
import numpy as np

reader = csv.reader('the_web.csv')


# importing csv sheet 
raw_people =[]
with open('the_web.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        raw_people.append(row)

#making people object list
people = []
for i in raw_people:
    people.append(Person(i[0],i[1:]))

#creating vertices

g = Graph()
g.add_vertices(len(people))
summary(g)

#assiging names
index = 0
for i in people:
    g.vs["name"] = [i.getName() for i in people]
    g.vs["size"] = [len(filter(None,i.getConnections()))*5 for i in people]
    index+=1

print g.vs[0]
#create a dict to lookup id's of people to assign edges to them
dict = {}
for i in people:
    dict[i.getName()] = i.getId()
    dict["size"] = len(filter(None,i.getConnections()))*5
#print dict

#add EdgeS
for i in people:#loop through people
    for conn in i.getConnections():#loop thorugh that persons connections
        #find id of Person
        if conn:
            print ("conn = "+ conn)
            id_of_conn = dict[conn]
            g.add_edge(i.getId(),id_of_conn)

g.vs["label"] = g.vs["name"]

#print [i.getId() for i in people]
layout = g.layout("kk")
plot(g,"the_web.png",layout = layout, margin = 20, autocurve= False)
g.save("the_web.dot")
#g.save("the_web.PNG")
