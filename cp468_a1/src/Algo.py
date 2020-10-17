'''
Created on 2020 M10 14

@author: Danni
'''

import generate_puzzle


class algo(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def h1(self, currState, goalState):
        
        mismatch = 0
        for i, j in zip(currState, goalState):
            for m, n in zip(i, j):               
                if m != n and m != 0:
                    mismatch += 1
        print("Mismatch: ", mismatch)
                
        return mismatch
    
    def h2(self, currState, goalState):
        
        dist = 0
        for i in range(len(currState)):
            for j in range(len(currState[i])):
                
                numb = currState[i][j]
                for k, x in enumerate(goalState):
                    if numb in x:
                        a = k
                        b = x.index(numb)
   
                if i == j and a == b:
                    if abs(i - a) == 1:
                        dist += 2
                    elif abs(i - a) == 2:
                        dist += 4
                elif i == a:
                    if abs(j - b) == 1:
                        dist += 1
                    elif abs(j - b) == 2:
                        dist += 2
                elif j == b:
                    if abs(i - a) == 1:
                        dist += 1
                    elif abs(i - a) == 2:
                        dist += 2
                elif i == b and j == a:
                        dist += 2
                elif i == j and i != 0 and a == b:
                    dist += 2
                else:
                    dist += 3
                    
        return dist
        
    # open list
    # contains all the nodes that are being generated and don't exist in closed list
    # initially holds the start node
    # next node chosen from the open list is based on its f score (heuristic); node with the least f score is explored
    
    # closed list
    # after a node is explored, it's put in the closed list and its neighbors are put in the open list
    # each node has a pointer to its parent so that at any given point it can retrace the path to the parent
        
