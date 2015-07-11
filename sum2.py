import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag

def tf(word,document):
	frequency=0
	for words in document :
		if words == word :
			frequency= (frequency+1)
	return frequency

def cf(word,documentlist):
	frequency=0
	for document in documentlist :
		frequency= (tf(word,document))+ frequency
	return frequency

def df(word,documentlist):
	frequency=0
	for document in documentlist:
		if tf(word,document)>0 :
			frequency = 1+frequency
	return frequency 

def N(documentlist):
	n=0
	for document in documentlist:
		n=1+n
	return n

def S(word,documentlist):
	return ((float((cf(word,documentlist)))/(df(word,documentlist)))-1)

def T(word,documentlist):
	return (float((cf(word,documentlist)))/(N(documentlist)))

def R(word,documentlist):
	return T(word,documentlist)/S(word,documentlist)

def delta(k):
	if k==0 :
		return 1 
	else :
		return 0

def probfirst(word,document,documentlist):
	return (1-R(word,documentlist))*delta(tf(word,document))

def probsecond(word,document,documentlist):
	return R(word,documentlist)/(1+(S(word,documentlist)))


def exponent(x,y):
	if y==1 :
		return x
	return x*exponent(x,(y-1))

def probthird(word,document,documentlist):
	return exponent((S(word,documentlist)/1+S(word,documentlist)),tf(word,document))

def probabilityword(word,document,documentlist):
	return probfirst(word,document,documentlist) + (probsecond(word,document,documentlist) * probthird(word,document,documentlist))

def tokdoclist(documentlist):
	return [ (word_tokenize(doc)) for (doc) in (documentlist)]

def probabilitysentenceuntok(sentence,document,documentlist):
	value=0
	for word in sentence:
		value=(probabilityword(word,(word_tokenize(document)),(tokdoclist(documentlist))))+value
	return value

def probabilitysentence(sentence,document,documentlist):
	probabilitysentenceuntok((word_tokenize(sentence)),document,documentlist)

def probabilitysentencelist(document,documentlist):
	sentencelist = sent_tokenize(document)
	return [probabilitysentence(sentence,document,documentlist)for sentence in sentencelist]


























