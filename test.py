def sp(x):
	if x == "healthy":
		return 0.6
	else:
		return 0.4


def tp(x,y) :
	if (x,y) == ("healthy","healthy") :
			return 0.7
	elif (x,y) == ("healthy","fever") :
		return 0.3
	elif (x,y) == ("fever","healthy") :
		return 0.4
	else :
		return 0.6
                   	
def ep(x,y):
	if (x,y)==("healthy","normal"):
		return 0.5
	elif (x,y)==("healthy","cold"):
		return 0.4
	elif (x,y) ==("healthy","dizzy"):
		return 0.1
	elif (x,y)==("fever","normal"):
		return 0.1
	elif (x,y)==("fever","cold"):
		return 0.3
	else :
		return 0.6

def eplist(observation,statelist):
    return [ep(state,observation) for state in statelist]
def epmatrix(observationlist,statelist):
    return [eplist(observation,statelist) for observation in observationlist]
 
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


