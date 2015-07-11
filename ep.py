def maxl(l):
    myMax = float('-inf')
    for i in l:
        if i > myMax:
            myMax = i
    return myMax

def transition(x,y) :
    if (x,y) == (0,0) :
            return 0.7
    elif (x,y) == (0,1) :
        return 0.3
    elif (x,y) == (1,0) :
        return 0.4
    else :
        return 0.6

def mult(list1,bitem,b):
    return maxl([bitem*a*transition(list1.index(a),b.index(bitem)) for a in list1]) 
def multmaxlists(list1,b):
    return[mult(list1,bitem,b) for bitem in b]