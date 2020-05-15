"""

"""

class Transversals:
    """
    At the time of starting the repo, this was part of hypergraph,
    hence all sorts of things may be broken now
    """

    def __init__(self):
        pass

    def _newtransv(self,currtrs,newtr):
        """
        Find a new minimal transversal of self
        'new' means not covered by the current transversals currtrs
        currtrs must consist initially only of transversals of self
        returns True if a new transversal found in newtr
        returns False if no new transversals exist: currtrs is the tr h of self
        """

        self.updatecarrier()
        
        if len(self.hyedges)==0:
            if currtrs.somempty():
                return False
            else:
                newtr = set([])
                return True
        elif self.somempty():
            return False
        else:
            selflocal = hypergraph()
            currlocal = hypergraph()
            for el in self.carrier:
                "try el not in newtr"
                self._xcopy(selflocal)
                currtrs._xcopy(currlocal)
                selflocal.remel(el)
                currlocal.remed(el)
                if selflocal._newtransv(currlocal,newtr):
                    return True
                else:
                    "try el in newtr"
                    self._xcopy(selflocal)
                    currtrs._xcopy(currlocal)
                    selflocal.remed(el)
                    currlocal.remel(el)
                    fd = selflocal._newtransv(currlocal,newtr)
                    if fd:
                        newtr.add(el)
                        return True
                    else:
                        return False

    def transv(self):
        """
        Find the hypergraph of minimal transversals of self
        """
        currtrs = hypergraph()
        newtr = set([])
        while self._newtransv(currtrs,newtr):
            currtrs.added(newtr.copy())
            newtr = set([])
        return currtrs

