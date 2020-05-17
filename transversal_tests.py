"""
If moved down to tests/, would NOT work anymore, 
because hytra is not known in that directory.

How NOT to make up for that:
- adding single dots before hytra raises "'__main__' is not a package"
- adding double dots before hytra raises 
    "attempted relative import beyond top-level package"
"""


from hytra import HyperGraph as hypergraph
from hytra import Transversals as T

if __name__ == "__main__":
	
    h = hypergraph()

    h.added(set(['A']))
    h.added(set(['B']))

    h.added(set(['A','B']))
    h.added(set(['B','C']))
    h.added(set(['B','D']))
    h.added(set(['C','D']))

    h.added(set(['A','B','C']))
    h.added(set(['B','C','D']))
    print(h.hyedges)


    t = hypergraph()
    a = T()
    t = a.transv_z(h)
    print(t.hyedges)


    h = hypergraph(set(['1','2']),[set('1'),set('2')])
    print(h.hyedges)

    t = hypergraph()
    t = a.transv_z(h)
    print(t.hyedges)

