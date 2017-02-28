from person import Person
from igraph import *
import csv
#import numpy as np
#import pygraphviz

scale_size = 3

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
print ("Creating Nodes...")
g = Graph()
g.add_vertices(len(people))
#summary(g)

#assiging names
print ("Naming nodes...")
index = 0
for i in people:
    g.vs["name"] = [i.getName() for i in people]
    g.vs["size"] = [len(filter(None,i.getConnections()))*scale_size for i in people]
    index+=1


#create a dict to lookup id's of people to assign edges to them
dict = {}
for i in people:
    dict[i.getName()] = i.getId()
    dict["size"] = len(filter(None,i.getConnections()))*5
#print dict

#add EdgeS
print ("Building Connections")
for i in people:#loop through people
    for conn in i.getConnections():#loop thorugh that persons connections
        #find id of Person
        if conn:
            print ("\t"+i.getName() +"--"+ conn)
            id_of_conn = dict[conn]
            g.add_edge(i.getId(),id_of_conn)

g.vs["label"] = g.vs["name"]

#print [i.getId() for i in people]
layout = g.layout("fr")#kk or drl, or fr
plot(g,"the_web.png",layout = layout, margin = 20, autocurve= False)
g.save("the_web.dot")
#g.save("the_web.PNG")
