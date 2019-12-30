import random

if __name__ == "__main__":


    def Composition(Text, k):
        comp=list()
        for i in range(len(Text)-k+1):
            comp.append(Text[i:i+k])

        return comp

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

    def OverlapGraph(Pattern):
        adjList ={}
        for node in Pattern:
            adjList[node] = []

        for node in adjList:
            for patt in Pattern:
                 if Suffix(node) == Prefix(patt):
                    adjList[node].append(patt)

        return adjList

    def deBruijnGraph(Text, k):
        node=dict()
        edge=dict()
        for i in range(len(Text) - k + 1):
            x=Text[i:i+k-1]
            node[x]=[]
        for i in range(len(Text) - k + 1):
            x=Text[i:i+k]
            nod=Prefix(x)
            node[nod].append(Suffix(x))

        return node

    def deBruijnEdgeGraph(Patterns):
        node=dict()
        for pattern in Patterns:
            node[Prefix(pattern)] = []
        for pattern in Patterns:
            node[Prefix(pattern)].append(Suffix(pattern))
        return node

    def EulerianCycle(Graph):
        Cycle=list()

        #NODELIST + FIRST NODE
        nodeKey=Graph.keys()
        nodeList=[]
        for key in nodeKey:
            nodeList.append(key)

        v0 = nodeList[0]
        Cycle.append(v0)
        x=True
        while x:
            edgeList=Graph[v0]
            if edgeList:
                rand=random.choice(edgeList)
                edgeList.remove(rand)
                Graph[v0]=edgeList
                v0=rand
                Cycle.append(v0)

            else:
                x=False
        #print(Cycle)
        x=False
        for nodes in Cycle:
            if Graph[nodes]:
                x=True
        x=True

        y=True
        newNodeStart=0
        while x:
            #check and set newNodeStart enters exit protocol if no edges exists for the nodes
            override=False
            for nodes in Cycle:
                if Graph[nodes]:
                    newNodeStart=nodes
                    override=True
            x=override

            #Find the Index for the node w edges and creates the cycle with that node being the starting pt
            index=Cycle.index(newNodeStart)
            top=Cycle[index:len(Cycle)]
            bottom=Cycle[1:index+1]
            CyclePrime=list()
            top.extend(bottom)

            #parses through Graph to generate another Cycle
            while y:
                edgeList=Graph[newNodeStart]
                if edgeList:
                    rand = random.choice(edgeList)
                    edgeList.remove(rand)
                    Graph[newNodeStart] = edgeList
                    newNodeStart = rand
                    CyclePrime.append(newNodeStart)
                else:
                    y=False

            #merges the cycles
            top.extend(CyclePrime)
            Cycle=top
            #print(top)

            y=True
        print(Cycle)
        return Cycle

    def EulerianPath(Graph):
        Cycle=list()
        inDegree=0
        outDegree=0
        v0=0
        vF=0
        nodes=Graph.keys()
        #Find First Node(node with outdegree greater than indegree)
        #wait=input("press enter to cont 1")
        for node in nodes:
            outDegree=len(Graph[node])
            for n in nodes:
                for edge in Graph[n]:
                    if edge==node:
                        inDegree+=1
            if inDegree < outDegree:
                v0=node
                #print(inDegree,outDegree,node)
            if inDegree > outDegree:
                vF=node
                #print(inDegree,outDegree,node)
            inDegree=0
            outDegree=0

        newNode=v0
        Cycle.append(v0)
        #print(Cycle)
        #wait = input("press enter to cont 2")
        #Find Final Node(edge that has no node)
        if vF == 0 or vF == "":
            for node in nodes:
                for edge in Graph[node]:
                    if (edge not in nodes):
                        vF=edge
        #print(v0,vF)

        #generate first Path
        x = True
        #wait = input("press enter to cont 3")
        while x:
            if newNode != vF:
                edgeList=Graph[newNode]
                rand = random.choice(edgeList)
                edgeList.remove(rand)
                Graph[newNode] = edgeList
                newNode = rand

                Cycle.append(newNode)
            else:
                x=False
        #print(Cycle)
        #figure out boolean if sum of all edgelists is 0
        count=0
        #wait = input("press enter to cont 4")
        for node in nodes:
            for edge in Graph[node]:
                count+=1
        if count != 0:
            x=True

        #wait=input("enter")
        #while loop to add to list
        y=True
        CyclePrime=[]
        #wait = input("press enter to cont 5")
        while x:
            #finds node in graph that has an edge and in cycle
            for node in nodes:
                if node in Cycle and Graph[node]:
                    newNode=node
            CyclePrime.append(newNode)
            newNodeStart=newNode
            #print(newNode)
            #generates the internal Cycle at newNodeStart
            #wait = input("press enter to cont 6")
            #print(Graph)
            while y:
                edgeList=Graph[newNode]
                #print(edgeList)
                if edgeList:
                    rand=random.choice(edgeList)
                    edgeList.remove(rand)
                    Graph[newNode] = edgeList
                    newNode = rand
                    CyclePrime.append(newNode)
                else:
                    y=False
            y=True
            #print(CyclePrime)
            #adds the cycleprime to cycle
            ind=Cycle.index(newNodeStart)
            before=Cycle[0:ind]
            after=Cycle[ind+1:len(Cycle)]
            CyclePrime.extend(after)
            before.extend(CyclePrime)
            Cycle=before
            CyclePrime=[]
            #print(Cycle)
            #check to see if we can exit the loop
            count = 0
            for node in nodes:
                for edge in Graph[node]:
                    count += 1
            if count != 0:
                x = True
            else:
                x=False
        #print(Cycle)





        return Cycle

    def StringReconstruction(k,Patterns):
        deBruijnGraph=deBruijnEdgeGraph(Patterns)
        print(deBruijnGraph)
        ConstructPath=EulerianPath(deBruijnGraph)
        print(ConstructPath)
        Construct=PathToGenome(ConstructPath)
        print(Construct)
        return Construct

    def Prefix(Text):
        return Text[0:len(Text)-1]
    def Suffix(Text):
        return Text[1:len(Text)]

    def de_bruijn(k, n):
        """
        De Bruijn sequence for alphabet size k
        and subsequences of length n.
        """
        a = [0] * k * n
        sequence = []

        def db(t, p):
            if t > n:
                if n % p == 0:
                    for j in range(1, p + 1):
                        sequence.append(a[j])
            else:
                a[t] = a[t - p]
                db(t + 1, p)
                for j in range(a[t - p] + 1, k):
                    a[t] = j
                    db(t + 1, t)

        db(1, 1)
        print(sequence)
        return sequence

    def StringToPairedReads(k,d,Text):
        LongRead=[]
        for i in range(len(Text)-2*k-d+1):
            read1=Text[i:i+k]
            read2= Text[i + k + d:i + k + d + k]
            t=(read1,read2)
            LongRead.append(t)

        return LongRead

    def PrefixPaired(PairedRead):
        PreRead1=Prefix(PairedRead[0])
        PreRead2=Prefix(PairedRead[1])
        PreRead=(PreRead1,PreRead2)
        return PreRead
    def SuffixPaired(PairedRead):
        SufRead1 = Suffix(PairedRead[0])
        SufRead2 = Suffix(PairedRead[1])
        SufRead = (SufRead1, SufRead2)
        return SufRead

    def deBruijnEdgeGraphPaired(PairedReads):
        graph={}
        for pr in PairedReads:
            graph[PrefixPaired(pr)]=[]
        for pr in PairedReads:
            graph[PrefixPaired(pr)].append(SuffixPaired(pr))
        return graph

    def StringSpelledByGappedPatterns(k,d,PairedPath):
        String=""



        n=len(PairedPath)
        for p in PairedPath:
            print(p)
            first=p[0]
            first=first[0]
            String+=first
        print(String)
        lastString=PairedPath[n-1]
        lastString=lastString[0]
        lastString=lastString[1:k]
        String+=lastString
        print(String)
        for pr in PairedPath[n-d-k+2:n]:
            second=pr[1]
            second=second[0]
            String+=second
            print(String)
        lastString=PairedPath[n-1]
        lastString=lastString[1]
        lastString=lastString[1:k]
        String+=lastString

        return String

    def StringReconstructionPairedReads(k,d,PairedReads):
        graph=deBruijnEdgeGraphPaired(PairedReads)
        for a in graph:
            print(a,graph[a])
        Path=EulerianPath(graph)
        #for p in Path:
            #print(p)
        String=StringSpelledByGappedPatterns(k,d,Path)
        return String











#    #print StringReconstructionPaired
    '''
    f=open("StringReconstructionPaired.txt","r")
    pt = f.readlines()
    pattern = []

    # print(pattern)
    for p in pt:
        prt = p.strip('\n')
        prt = prt.replace("|"," ")
        strings=prt.split()
        t=(strings[0],strings[1])
        pattern.append(t)


    k=50
    d=200

    s=StringReconstructionPairedReads(k,d,pattern)
    print(s)
    '''
    '''ans=deBruijnEdgeGraphPaired(ans)
    Path=EulerianPath(ans)
    StringSpelledByGappedPatterns(2,3,Path)
    for p in Path:
        print(p)'''

#    #print StringReconstruction
    '''
    f=open("StringReconstruction.txt","r")
    pt = f.readlines()
    pattern = []

    # print(pattern)
    for p in pt:
        prt = p.strip('\n')
        pattern.append(prt)
    k=4
    StringReconstruction(k,pattern)
'''
#    print k-universal de_bruijn
    '''ans=de_bruijn(2,k)
    printable=""
    for s in ans:
        printable+=str(s)
    print(printable)'''
#    #Changing arrowed input into dictionary
    '''
    f = open("inputEulerianPath.txt","r")
    if f.mode == "r":
        grp=f.readlines()

    graph={}
    edgeList=[]
    for g in grp:
        gg=g.strip("\n")
        ggg=gg.rpartition(" -> ")
        ggg=list(ggg)
        ggg.remove(" -> ")
        node=int(ggg[0],10)
        edgeString=ggg[1].replace(","," ")
        edgeList=edgeString.split()

        graph[node]=[]
        for e in edgeList:
            graph[node].append(int(e,10))

    #Print EulerianCycle

    ans=EulerianPath(graph)
    fo = open("file.txt","w")
    for i in range(len(ans)):
        intI=str(ans[i])
        if i != len(ans)-1:
            fo.writelines(intI + "->")
        else:
            fo.writelines(intI)

'''
#    #print deBruijnEdgeGraph
    '''
    fo = open("file.txt","w")
    f = open("inputdBEG.txt","r")
    Patterns = []
    if f.mode == "r":
        path = f.readlines()
    for p in path:
        prt = p.strip('\n')
        Patterns.append(prt)
        


    ans=deBruijnEdgeGraph(Patterns)
    for a in sorted(ans):
        print(a,ans[a])

    for a in sorted(ans):
        if ans[a]:
            fo.writelines(a + " -> ")
            for b in range(len(ans[a])):
                if b != len(ans[a]) - 1:
                    fo.writelines(ans[a][b] + ",")
                else:
                    fo.writelines(ans[a][b])
            fo.writelines("\n")
    '''
#    #print deBruijnGraph
    '''
    fo = open("file.txt","w")

    Text="TGAGGATACCAACGCCAGTTAGCTAGATTTACACTGTAACCATGGTTAGAGATCGAGTTAATTATATCCAAGACGCGACTGGGGCCCGGATTCTTTAAGAGAGCTGCCAATCTTGTGGGACTTGCTGGTGAGGTGCCGGATGAGAGCTCAGGGTTCTAGTCTGCAGACGCAGACTATGTGCCAAGTGCGATGTTACACCTGGCAGATCTTTAGCATAGTTACTGATTATGTCTAGTGGGGTGCTATATGCAAGCGGACAAGAACGCTGTAGTATTGTTCAATCGGCAACGTGCGTCCAGTGCACTGAGCCCGGCCCTCAGCTGCGGTAGAGGTGCGAAAATCATTATCTCAGATTTTAAGTTACGAGTTTTAATTTGTTCTCTCATCAAATCCGTGCGCTACTTAATTAGAGGCTACCCTGAAGACCTGTGACTGAAGAATTCACCACCGCGAGCTACGGCAGCTGTACCGAGCCACCATCGAGTGTGGAGGCCCCTAAGACGGACCGCGAACACCTGAGCGGCGGTTGATAGCCGCGCCGAAGTTTGGGTTCCCCTGGACGTGCGCCTTTGTGATACTGTTCGGAGGTAACATATTAACCGCTGCGAGAGAGAAGGCTTACGCGTGTGCAAATCACTTCCACAAGTTGCAAACGTCCCCGCCCTGTCGCGACTTACAGGCTACCACGGAATGCACTTGGAACAGGGGAGGACTGCGCTCTTGAAATGCTCCCACGCGTGCTGGAGCTTTACAATGGGGATGCGTCTCTGCGAGAAAGCCAATATCGAATCGACTGACGCGAATGGTGGAAGCATCGTCTTTACGGTTCGTGCAGATGTTTGAACTTTCGACGGAGCTGGGCGCGCGGAAGCGCGGCATTCCTCGGACTCGTAGATCGAGACCGGCTTTGATCTAGTAAAAAGTACCAACCACCTAAAAATCATCTCGTCGCTACAAAAATAACGTTCTCGAAATGTAGGATAGACCCAGCGTTTTGCGACCCGTTTCCCGACAGGGACAGACTTTGATCAGCCGGCTGCATAACTGGATACTGCCTTATACTATCGGATCGGAGCTAACTAGGATCTACCTCAATAGAGCAAAAAATCCCTAATTGGGAGACGTCGAAACTCTTGGTACTAGATAACAGAACAGACGGCAGAATGGGCCCCTAGCATCGTTATCGTAAGGCCACTCACGTCGGGATGGCATTGTTTTTCCCGCCTCTGGTGAACCTGTAGCTCGGCTAGCTGATTCGACGGGGCGTTCGGCTGGAGTACGGGTTGTACAAAGGTGAAAAGTGCACATAACGGAACTATCAACTTCTCTCAGAGAGCTGCGCTGGGGGAGGTCGTTCCGCCGGGTGAAGAGCGTGAAACCCTACCTTCATCTATACCTCCGACTACTGGCGATATAGACCATGCTAACAGGCGCTTCAGGGTAATACACAGCATTTAACCTTAGGCTTCACAGGTCTTTGTCCGGGTCCGACCCGCGCATCCTGACGTCGCGAAAGTTAATACCATAGGGCGTAGGAAGAACGGCAAGCGGGCATAAGCGACGTTTAATCCCAGTAACGAGCTTGAGGGTGTACATACCTTCGGGTTTGTTGCTCTAGCGGCGCAAGATTCGGAGATCTCAGTCTTCGTACGAGATTTTTATTACCATGCAGAAAAACCCCCGGACGGTTACACATAGCGTCCCTCGGAGAGTTTGGTGTATTCACAAGGTTATTTTTGCAAAATTTGAGGGTGATACAACCGTCCTAAGGAGAAGATGGACTCACCTACCCAGCACGCACGCTCGCCCGTCCCGCGACGGCGGCGAAACATGCTCCTGTCGAGGTGCGCCCAGCCTGTTGGTGCCACCTCGCCGAACATGATCTTCTCCCGGTCCTAAAAAGAATTGCCTCAGTGTCCCACGACGAAGTGTCCCACGGCAAGCTCAGTAGAGAGGCTTAGTATGAAAGAGCGGGGACTACCTGAATCTTACGGGGGGGA"
    k=12
    
    ans = deBruijnGraph(Text,k)
    for a in sorted(ans):
       print(a,ans[a])


    for a in sorted(ans):
        if ans[a]:
            fo.writelines(a + " -> ")
            for b in range(len(ans[a])):
                if b != len(ans[a])-1:
                    fo.writelines(ans[a][b] + ",")
                else:
                    fo.writelines(ans[a][b])
            fo.writelines("\n")
            '''

#    #print OverlapGraph
    """f=open("inputOG.txt",'r')
    pt=f.readlines()
    pattern=[]
    fo=open("file.txt",'w')
    #print(pattern)
    for p in pt:
        prt = p.strip('\n')
        pattern.append(prt)
    print(pattern)
    ans = OverlapGraph(pattern)
    for a in ans:
        if ans[a]:
            fo.writelines(a+" -> ")
            for b in range(len(ans[a])):
                fo.writelines(ans[a][b]+ " ")
            fo.writelines("\n")"""

#    #print PathToGenome
    """f = open("dataset198PG.txt" , "r")
    pt=[]
    if f.mode == "r":
        path=f.readlines()
    for p in path:
        prt=p.strip('\n')
        pt.append(prt)

    #print(pt)
    ans=PathToGenome(pt)

    for a in ans:
        print(a)"""