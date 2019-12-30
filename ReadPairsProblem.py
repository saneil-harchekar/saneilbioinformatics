import networkx as nx
if __name__ == "__main__":
    array=["GAGA|TTGA",
     "TCGT|GATG",
     "CGTG|ATGT",
     "TGGT|TGAG",
     "GTGA|TGTT",
     "GTGG|GTGA",
     "TGAG|GTTG",
     "GGTC|GAGA",
     "GTCG|AGAT"]
    f = open("StringReconstructionPaired.txt","r")
    pat=f.readlines()
    array.clear()
    for line in pat:
        string=line.strip("\n")
        array.append(string)
    #print(array)
    #for line in array:
        #s = line.translate(None, '\n')
        #array.append(s)
    k = 50
    d=200
    def Graph(array, k):
        graph = {}
        for string in array:
            prefix = string[0:k - 1] + string[k] + string[k + 1:2 * k]
            suffix = string[1:k] + string[k] + string[k + 2:]
            graph[prefix] = [suffix]
        return graph


    f = open("MaximalPath.txt", "r")
    if f.mode == "r":
        grp = f.readlines()
    l=0
    graph = {}
    edgeList = []
    for g in grp:
        g = g.strip("\n")
        g = g.rpartition(" -> ")
        g = list(g)
        g.remove(' -> ')
        node = int(g[0], 10)
        edgeString = g[1].replace(",", " ")
        edgeList = edgeString.split()

        graph[node] = []
        for e in edgeList:
            graph[node].append(int(e, 10))

    #l = len(Graph(array, k))
    #print(l,Graph(array,k))
    #ans=Graph(array,k)
    #for a in ans:
     #   print(a,ans[a])
    #print(G)
    '''
    graph={1: [2],
           2: [3],
           3: [4,5],
           6: [7],
           7: [6]}
    '''
    Gr = nx.DiGraph(graph)
    print(Gr)


    def EulerPath(G):
        nodes = list(G.nodes())
        path=[]
        for node in nodes:
            if G.in_degree(node) < G.out_degree(node):

                node, G.in_degree(node), G.out_degree(node)
                path = list(nx.dfs_edges(G, node))  # list(Allpath(G, node))
                break
        string = path[0][0][:k - 1]
        for i in range(0, len(path)):
            string += path[i][1][k - 2]
        for j in range(l - k - d, len(path)):
            string += path[j][1][-1]
        print(string)

    def MaximalNonBranchingPaths(Graph):
        nodes=Graph.nodes()
        path=[]
        Paths=[] #paths <-- empty list
        for node in nodes: #for each node v in Graph
            if not (Graph.in_degree(node) == 1 and Graph.out_degree(node) == 1): #if v is not a 1-in-1 out node
                if Graph.out_degree(node) > 0: #if outdegree of node v is greater than 0
                    edgeList=Graph.edges(node) #initializing edge list such that we can parse through every edge
                    for edge in edgeList: #for each out going edge (v,w) from v
                        path.append(edge[0])
                        w=edge[1] #edge = (v,w)
                        path.append(w) #NonBranchingPath <-- the path consisting of the single edge (v,w)
                        edgeListOfW=Graph.edges(w)
                        while Graph.in_degree(w)==1 and Graph.out_degree(w)==1: #while w is a 1-in-1 out node
                            edgeOfW=Graph.edges(w) #if 1-in-1-out then only one edge will exist
                            for e in edgeOfW:
                                path.append(e[1])
                                w=e[1]
                        copy=path.copy()
                        path.clear()
                        Paths.append(copy)


        SimpleCycles=list(nx.simple_cycles(Graph))
        for cycle in SimpleCycles:
            cycle.append(cycle[0])
            Paths.append(cycle)

        #print(Paths)
        return Paths


    def Prefix(Text):
        return Text[0:len(Text) - 1]
    def Suffix(Text):
        return Text[1:len(Text)]

    def PathToGenome(Path):
        pLen=len(Path)
        retString=Path[0]
        #print(retString)
        stringLen=len(retString)
        for i in range(1,pLen):
            temp=Path[i]
            retString += temp[stringLen-1]
            #  print(retString)
        return retString

    def deBruijnEdgeGraph(Patterns):
        node=dict()
        for pattern in Patterns:
            node[Prefix(pattern)] = []
        for pattern in Patterns:
            node[Prefix(pattern)].append(Suffix(pattern))
        return node

    def Contigs(Patterns):
        Graph=deBruijnEdgeGraph(Patterns)
        print(Patterns)
        print(Graph)
        Gr = nx.MultiDiGraph(Graph)
        paths=MaximalNonBranchingPaths(Gr)
        print(paths)
        stringMax=[]
        for path in paths:
            stringMax.append(PathToGenome(path))

        print(stringMax)
        return stringMax

    f = open("ContigStrings.txt","r")
    fo = open("file.txt","w")
    pat = f.readlines()
    patterns=[]
    for p in pat:
        p=p.strip("\n")

        patterns.append(p)
    ans=Contigs(patterns)

    for a in ans:
        fo.writelines(a + " ")

    '''
    ans = MaximalNonBranchingPaths(Gr)
    f=open("file.txt","w")
    for a in ans:
        for i in range(len(a)):
            string=str(a[i])
            if i != len(a)-1:
                f.writelines(string + " -> ")
            else:
                f.writelines(string+"\n")
    '''

