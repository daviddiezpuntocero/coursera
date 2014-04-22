class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    if (atMe.myName() > newFrob.myName()):
        if (atMe.getBefore() == None):
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        elif (atMe.getBefore().myName() <= newFrob.myName()):
            ob = atMe.getBefore()
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            newFrob.setBefore(ob)
            ob.setAfter(newFrob)
        else:
            insert(atMe.getBefore(), newFrob);
    elif (atMe.myName() <= newFrob.myName()):
        if(atMe.getAfter() == None):
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif(atMe.getAfter().myName() >= newFrob.myName()):
            oa = atMe.getAfter()
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
            newFrob.setAfter(oa)
            oa.setBefore(newFrob)
        else:
            insert(atMe.getAfter(), newFrob)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    # Your Code Here
    print start.myName()
    print start.getBefore()
    if start.getBefore() == None:
        print "returning", start.myName()
        return start
    else:
        return findFront(start.getBefore())

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)


p = Frob('percival')
r = Frob('rupert')
insert(p, r)

# findFront(p)
print findFront(r).myName()
