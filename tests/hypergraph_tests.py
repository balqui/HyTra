"""
Python 2 legacy code to update
"""


if __name__ == "__main__":
	"TOO MANY print TO CORRECT THEM ALL, TESTS JUST HIDDEN"
	pass
	
    # ~ print "slatt module hypergraph called as main and running as test"

    # ~ h = hypergraph()

# ~ #    small tests

    # ~ h.added(set(['A']))
    # ~ h.added(set(['B']))

    # ~ h.added(set(['A','B']))
    # ~ h.added(set(['B','C']))
    # ~ h.added(set(['B','D']))
    # ~ h.added(set(['C','D']))

    # ~ h.added(set(['A','B','C']))
    # ~ h.added(set(['B','C','D']))

    # ~ print "h has 8 hyedges on A, B, C, D"
    # ~ print h.carrier
    # ~ print h.hyedges

# ~ # must add testing for addhg etc

    # ~ hh = h.copy()
# ~ ##    hhh = hypergraph()
# ~ ##    h.xcopy(hhh)

    # ~ h.added(set(['A','D']))

    # ~ h.simplify()
# ~ #    h.simplify({'A':['B','C']})

    # ~ print "h modified: added AD and simplified:"
    # ~ print h.carrier
    # ~ print h.hyedges

    # ~ print "hh, a copy of h before modification:"
    # ~ print hh.carrier
    # ~ print hh.hyedges

# ~ ##    print "hhh, an xcopy of h before modification:"
# ~ ##    print hhh.carrier
# ~ ##    print hhh.hyedges


    # ~ t = hypergraph()
    # ~ t = h.transv()

    # ~ print "h again:"
    # ~ print h.carrier
    # ~ print h.hyedges
    # ~ print "t, its transversal:"
    # ~ print t.carrier
    # ~ print t.hyedges

    # ~ h = hypergraph(set(['1','2']),[set('1'),set('2')])

    # ~ print "fully changed h"
    # ~ print h.carrier
    # ~ print h.hyedges

    # ~ print "did t change as well?"
    # ~ print t.carrier
    # ~ print t.hyedges

    # ~ t = hypergraph()
    # ~ t = h.transv()

    # ~ print "initialized h and its transversal"
    # ~ print h.carrier
    # ~ print h.hyedges
    # ~ print t.carrier
    # ~ print t.hyedges

    # ~ print "another hypergraph hh on different universe"
    # ~ hh = hypergraph(set(['1','2','3']),[set(['1','2']),set(['2','3'])])
    # ~ print hh.carrier
    # ~ print hh.hyedges


