from Graph import graph

graph = graph({ "a" : [("b", 3)],
          "b" : [("c", 2), ("d", 6), ("e", 2), ("f", 8)],
          "c" : [("b", 2), ("d", 5)],
          "d" : [("c", 5), ("b", 6)],
          "e" : [("b", 2), ("f", 1)],
          "f" : [("e", 1), ("b", 8)]
        })

graph.print_edges()
#start at a
#end at f

      

graph.dijsktra("a", "f")
