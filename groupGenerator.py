"""
Owen Chapman
1/26/2017
Experience of God
Group generator

Yes, I'm aware the code is hacky. Yes, I'm even aware that it's incorrect.
No, I don't care. It's adequate for its commission.

TODO:
Javascript / HTML for user interface?
format and read accompanying files: roster.txt, groups.txt
"""

import numpy as np
import itertools

names = []
genders = []
namedict = {}
nstudents=0


def run():
    global nstudents
    global groupmatrix
    global groupsizes
    #PARAMETERS
    groupsizes = [5,5,5]
    
    #GLOBAL VARIABLES

    readroster()
    nstudents=len(names)
    readgroups()

    grouping = dumb()
    prettyprint(grouping)


def gengroup():
    return [range(0,5),range(5,9),range(9,14)]
def genrandgroup():
    pass
def evalgroup(grouping):
    cost=0
    #grouping a list [[],[],[]]
    for group in grouping:
        for i in range(len(group)):
            for j in range(0,i):
                cost+=(groupmatrix[group[i]][group[j]])**2
        numF = 0
        for i in range(len(group)):
            if genders[group[i]]=='F':
                numF+=1
        if numF == 1:
            cost+=15
        elif numF == 0:
            cost+=10
    return cost
def prettyprint(grouping):
    for group in grouping:
        printval=[]
        for i in range(len(group)):
            printval.append(names[group[i]])
        print printval

def dumb(steps=10000):
    """
    Generates 1000 pairings, evaluates them, keeps best"
    """
    best = gengroup()
    bestcost = evalgroup(best)
    for s in range(steps):
        g=np.random.permutation(nstudents)
        group=[]
        for size in groupsizes:
            group.append(g[(-1*size):])
            g=g[:(-1*size)]
        cost=evalgroup(group)
        if cost<bestcost:
            bestcost=cost
            best=group
    print "cost:",bestcost
    return best

def readroster():
    global names
    global genders
    global namedict
    count=0
    with open('roster.txt') as f:
        for line in f:
            if line[0]!='%':
                line=line.strip()
                line=line.split()
                names.append(line[0])
                genders.append(line[1])
                namedict[line[0]]=count
                count+=1
    #return (names,namedict)

def readgroups():
    global namedict
    global nstudents
    global groupmatrix
    groupmatrix = np.zeros((nstudents,nstudents),dtype=np.int)#nxn matrix
    with open('groups.txt') as f:
        for line in f:
            if line[0]!='%':
                line=line.strip()
                line=line.split()
                #convert to numerical index
                for i in range(len(line)):
                    line[i]=namedict[line[i]]
                #print line
                for ind in line:
                    for ind2 in line:
                        groupmatrix[ind][ind2]+=1
    #return groupmatrix

def pseudogenerate(steps=200,iters=3,startrate=.3):
    """
    Simulated annealing, saves best.
    steps: number of iterations in a single annealing
    iters: number of annealings
    startrate: annealing rate
    best=gengroup()
    bestcost=evalgroup(best)
    for it in range(iters):
        group=gengroup()
        cost=evalgroup(group)
        for s in range(steps):
            cg=
            cc=evalgroup(cg)
            if (cc<cost):
                cost=cc
                group=cg
            else:
    """    

run()
