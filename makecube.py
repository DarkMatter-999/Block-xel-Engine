pos = [
  [-1, -1, -1],
  [1, -1, -1],
  [1, 1, -1],
  [-1, 1, -1],
  [-1, -1, 1],
  [1, -1, 1],
  [1, 1, 1],
  [-1, 1, 1],
    ]


color = [
       [1,1,1], 
       [1,1,0],
       [1,0,1],
       [1,0,0],
       [0,1,1],
       [0,1,0],
       [0,0,1],
       [0,0,0],
    ]


for i in range(len(pos)):
    print("Vertex {position: ",[float(x) for x in pos[i]],", color: ",[float(x) for x in color[i]],"},")