"""
Must clean it up at some point
"""

from .hypergraph import HyperGraph as hypergraph

class Transversals:
    """
    At the time of starting the repo, this was part of hypergraph,
    hence all sorts of things may be broken now
    """

    def __init__(self):
        pass

    def _newtransv_z(self, hygr, currtrs, newtr):
        """
        Find a new minimal transversal of hygr
        'new' means not covered by the current transversals currtrs
        currtrs must consist initially only of transversals of hygr
        returns True if a new transversal found in newtr
        returns False if no new transversals exist: currtrs is the tr h of hygr
        """

        hygr.updatecarrier()
        
        if len(hygr.hyedges)==0:
            if currtrs.somempty():
                return False
            else:
                newtr = set([])
                return True
        elif hygr.somempty():
            return False
        else:
            selflocal = hypergraph()
            currlocal = hypergraph()
            for el in hygr.carrier:
                "try el not in newtr"
                hygr._xcopy(selflocal)
                currtrs._xcopy(currlocal)
                selflocal.remel(el)
                currlocal.remed(el)
                if self._newtransv_z(selflocal, currlocal, newtr):
                    return True
                else:
                    "try el in newtr"
                    hygr._xcopy(selflocal)
                    currtrs._xcopy(currlocal)
                    selflocal.remed(el)
                    currlocal.remel(el)
                    fd = self._newtransv_z(selflocal, currlocal, newtr)
                    if fd:
                        newtr.add(el)
                        return True
                    else:
                        return False

    def transv_z(self, hygr):
        """
        Find the hypergraph of minimal transversals of self
        """
        currtrs = hypergraph()
        newtr = set([])
        while self._newtransv_z(hygr, currtrs, newtr):
            currtrs.added(newtr.copy())
            newtr = set([])
        return currtrs

