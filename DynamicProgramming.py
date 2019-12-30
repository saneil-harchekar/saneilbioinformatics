import sys
import networkx as nx
if __name__ == "__main__":
    def DynamicChange(money, Coins):
        MinNumCoins=dict()
        MinNumCoins[0]=0
        for m in range(1,money+1):
            MinNumCoins[m]=float('Inf')
            for coin in Coins:
                if m >= coin:
                    if MinNumCoins[m-coin]<MinNumCoins[m]:
                        MinNumCoins[m]=MinNumCoins[m-coin]+1
        return MinNumCoins[money]


    def ManhattanTourist(n, m, Down, Right):
        s=[[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1,n+1):
            s[i][0]=s[i-1][0]+Down[i-1][0]
        for j in range(1,m+1):
            s[0][j]=s[0][j-1]+Right[0][j-1]
        for i in range(1,n+1):
            for j in range(1,m+1):
                s[i][j]=max(s[i-1][j]+Down[i-1][j],s[i][j-1]+Right[i][j-1])
        return s[n][m]

    def LCSBacktrack(StringA, StringB):
        s=[[0 for i in range(len(StringB)+1)] for j in range(len(StringA)+1)]
        Backtrack=[["" for i in range(len(StringB)+1)] for j in range(len(StringA)+1)]
        for i in range(1,len(StringA)+1):
            for j in range(1,len(StringB)+1):
                match=0
                if StringA[i-1]==StringB[j-1]:
                    match=1
                s[i][j]=max(s[i][j-1],s[i-1][j],s[i-1][j-1]+match)
                if s[i][j] == s[i][j-1]:
                    Backtrack[i][j]="R"
                elif s[i][j] == s[i-1][j]:
                    Backtrack[i][j]="D"
                elif s[i][j] == s[i-1][j-1]+match:
                    Backtrack[i][j]="RD"
        return Backtrack
    def OutputLCS(BT,v,i,j):
        if i == 0 or j == 0:
            return ""
        if BT[i][j] == "D":
            return OutputLCS(BT,v,i-1,j)
        elif BT[i][j] == "R":
            return OutputLCS(BT,v,i,j-1)
        else:
            return OutputLCS(BT,v,i-1,j-1)+v[i-1]
    def LCS(v,w):
        Backtrack=LCSBacktrack(v,w)
        i = len(v)
        j = len(w)
        sys.setrecursionlimit(2000)
        LCS = OutputLCS(Backtrack, v, i, j)
        return LCS

    def TopographicOrder(Graph_Unsorted):
        graph_sorted=0
        return graph_sorted

    def WeightedDigraphGenerator(Graph_Text):
        f=open(Graph_Text,"r")
        lines=f.read().splitlines()
        G={}
        nd_eg_wt = []
        for line in lines:
            line=line.replace("->"," ")
            line=line.replace(":"," ")
            intString=line.split()
            aList = []
            for i in intString:
                aList.append(int(i))
            nd_eg_wt.append(aList)
            #G.add_node.add_weighted_edge
            G[aList[0]]=list()
        for new in nd_eg_wt:
            G[new[0]].append((new[1],new[2]))

        Graph = nx.DiGraph()
        for key in G:
            for tup in G[key]:
                Graph.add_edge(key, tup[0], weight=tup[1])

        #print(G)
        return Graph





    def LongestPathDAG(source, sink, Graph_Text):
        G=WeightedDigraphGenerator(Graph_Text)
        pathLength={}
        for node in G.nodes:
            pathLength[node]=float("-inf")
        pathLength[source]=0
        GraphTopological=list(nx.topological_sort(G))
        print(GraphTopological)
        for i in range(len(GraphTopological)):
            a=G.in_edges(GraphTopological[i])
            weightList=[]
            #print(GraphTopological[i],a)
            if a:
                for edge in a:
                   weightAdd=G.get_edge_data(edge[0],edge[1])["weight"]
                   weightList.append((weightAdd,edge[0]))
                #print(weightList)
                pathLength[GraphTopological[i]] = max(weightList)[0]+pathLength[max(weightList)[1]]
            else:
                weightAdd=0
                weightList.append(weightAdd)
        #print(pathLength)
        currentNode=sink
        path=list()
        path.append(sink)
        while True:
            in_edge=G.in_edges(currentNode)
            lTemp=[]
            for e in in_edge:
                lTemp.append((pathLength[currentNode]-pathLength[e[0]],e[0]))
            #print(max(lTemp))
            path.append(max(lTemp)[1])
            currentNode=max(lTemp)[1]
            if currentNode == source:
                break
        path.reverse()
        #print(path)


        return (pathLength[sink],path)


    def calc_combinations(mass, coins):
        if mass == 0:
            return 1
        useful_coins = [coin for coin in coins if coin <= mass]
        if len(useful_coins) == 0:
            return 0
        if len(useful_coins) == 1:
            result = 1 if useful_coins[0] == mass else 0
            return result
        result = sum([calc_combinations(mass - i, coins) for i in coins])
        return result


    result = calc_combinations(21, [2,3])
    print(result)


    def Z(ep, sigma, omega, psi, q, beta):
        Z=[1]*10
        Zl=[1]*10
        for i in range(1,10):
            Z[i]= 1 + beta - ((q*beta)*(Z[i-1]-beta))/((Z[i-1]+ep*beta)*(Z[i-1]+sigma*beta))
            #print(Z[i])
        for i in range(1,10):
            Zl[i]= beta+(Zl[i-1])*(Zl[i-1])*(1+beta-Zl[i-1])/(q*beta)
            print(Zl[i])
        return Zl[9]
#print DynamicChange(money,Coins)
"""
    ans=DynamicChange(16845,[20, 16, 11, 5, 3, 1])
    print(ans)
    """

#print ManhattanTourist(n, m, Down, Right)
'''
f=open('ManhattanTourist.txt','r')
line=f.read().splitlines()
bool=True
l1=list()
l2=list()
#split inputs into l1 and l2 using the "-" to separate the two arrays
for string in line:
    if string == "-":
        bool=False
    if bool:
        l1.append(string)
    elif not bool and string != "-":
        l2.append(string)
#convert l1 into ints and Down Array
Down=list()
for string in l1:
    a=string.split(" ")
    temp=list()
    for b in a:
        temp.append(int(b))
    Down.append(temp)
#convert l2 into ints and Right Array
Right=list()
for string in l2:
    a=string.split(" ")
    temp=list()
    for b in a:
        temp.append(int(b))
    Right.append(temp)
ans=ManhattanTourist(6,5,Down,Right)
print(ans)
'''

#print LCS(StringA, StringB)
'''
v="GTGTAAATGTTGCTCTTTATCTGCCACTAGATTAACAATTTACGAGTATTAGCACCCTTCCCCCTAGCCGCATTAGCCCCGGAAAAGTCCGCATTCAAGCTTTAGCCTCAACCGGCGATCCCTGTAAACCCCTTCCCTCTGAATTAGCCTGTCCAAGTCAGCTAACTAGAAATCCGCTCGCTCGAATTGGCTCCGAGTAACGGGTTGCTCGAAAGCGCTCGTATATACTGAAAAGTTCTCATGGTAGCGGCTTCTAGATACGTCATGGGTGTGCGCGACGGGACCATGCACCTCTTGACAAGAGCATAGGAATTCTGAACCAGAAGTGTAGTTAACACCCACCTACGACACGACAAACGTGAACCAATAGTGAGTACTATAATCCAGGTTCTCGGTTTTGATCATTAGACATCAACCTAGTGACGAGAAGTCCTGATTCGGCTGGCCAAAACACAACTGCTCGCCCGTAGCACGTGCAAAGATGGGACGTGCCGTGAAGCCCTCCTCCCGCGCCGGGCGCAGAGCAGTACCCCCGCTTCGGCGGGAGACAGCTGGTATGGAGCTGGAATAAATCGCCTAGGATTAAGCAAGTGGCCTTCAGGCTTAATGTTCATCCCCAACACTCCAACAATGGGCCAAGTTCTTCAGTGGGAGATGGACTCTATCAGTTCACCACTCGTTTCTGACTAACGAACGGCGTAGAGGTACTTGTGCGACATACAGAGTGATGGGCTACCCGGTGTCCCAAAAGCCCACAAGCATGATTACACGAATCTCCAGCAATGTGCACATGGTTCAGGGGTCGTCAGGGGGTTACTGTGACACTCAGCATACTCGATACTCATGGAGCTGTGAAACAGAGAAATTACTTACCTAGGCTTCGTTCTACGTGACAGAAACTACGAGTC"
w="TAAATGTTCACTGTCTGGTTGAACTTCCCGCTTGGTTTTCACCTATTTCGTTCAGGTCACTGGTTAAGCCGCAATGGAGGATGTTCCCTCGGCGACATGCCGAGTACTAATTCGCGTGCCGGTCGTGCGAAATCGGAAAGTTCGCACCAGTACTACTACATATGTGGGGGGGATGATCAATATTCCAAGAGGTCGCGCTGGCTTAGGTCGACACTGATGCGTGGAAGCCCTCGGAGTGAGCAGTAGGGCAATGAAGGTGTATCACACTATCATCTGGACAGTCATGTTGATTCTTGTTCACCTGGTTTACAAGCGGGGAGCCGGTATGGCAGGAGGGTCCAAAGGGTCTTCAAACAGGTGCCCCAATATCACTAAGCGATGATACGCTATAGGCGAAATTGTAGCGAGAACTAAGATTCCTTACTTTTAACCTGTGTTAGTTCCTCCACAAAAGGTTATACTTCTAAGATGGGTTACATTCTAAGGTGTTTTAAGGTACGCCAGCCCGCCTTAGTCGGGGAAAGCCTGGGCCCCCCCTAAGCTGAACTATCCAAACCTAAGACCTATGACTTAAGCCTAGGAGCTATCCGGTGGTCAGCCAATGGTGTCGCGGGGGACGCATTATCGTGCCACAGCAGTAAAACAGACCGGGACACTAGTTACAGATAATTCGTAATTTTGACTCGCAGAGGTCTGGATTAACCGCTTGGCTAAAGATGCACGGACCGGTAGGATAACCAACTTAGGTTCAGTTAAGGAAATTTGGCACAGCTGGTCGGTCGATCTACCCGTCGGCGCGATTGGAGAGGTCATTATTCATTAACTGTTCGAAGCGAAGGGCCAATTTTATCCCTTGTAAGCAAACGTCAAAAGCAGCTTGAACCCTAAACGAATCCTGTGCCCGGTTCCACAAAAGTTGTCTTCTATGTGTGTGAACCGCAAGTCAACGCTGAGCTGTTCTTTGGTTATAGCGTTTTCGGGAATCCGTAACCTGAG"
ans=LCS(v,w)
print(ans)
'''

#print WeightedDigraphGenerator(Graph_Text)
'''ans=LongestPathDAG(0,44,"WeightedDigraph.txt")
f=open("file.txt","w")
f.writelines(str(ans[0])+"\n")
for i in range(len(ans[1])):
    string=str(ans[1][i])
    if i != len(ans[1])-1:
        f.writelines(string + "->")
    else:
        f.writelines(string+"\n")
'''
'''a=Z(0,0,1/8,27/64, 2.622, .0152)
print(a)
'''
