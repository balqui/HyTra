"""
Inside the hytra directory:
DOES NOT WORK because transversals imports from .hypergraphs

Would work if it would import from hypergraphs instead,
without the dot but, then, imports OUTSIDE this directory will fail
"""


from hypergraph import HyperGraph as hypergraph
from transversals import Transversals as T

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

