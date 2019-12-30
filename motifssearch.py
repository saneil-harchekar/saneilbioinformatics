import random
import math
if __name__ == "__main__":
    k=15
    t=20



    def RandomizedMotifSearch(Dna, k, t):
        M = RandomMotifs(Dna, k, t)
        BestMotifs = M

        while True:
            profile = ProfileWithPseudocounts(M)
            M = Motifs(profile, Dna)
            # print(Score(M),Score(BestMotifs))
            if Score(M) < Score(BestMotifs):

                BestMotifs = M
            else:
                return BestMotifs


    def RandomMotifs(Dna, k, t):
        randMotifs = []
        for i in range(t):
            x = random.randint(0, t)
            randMotifs.append(Dna[i][x:x + k])

        return randMotifs


    def Motifs(Profile, Dna):
        motifs = []
        t = len(Dna)
        k = len(Profile['A'])
        for i in range(t):
            motifs.append(ProfileWithMostProbablePattern(Dna[i], k, Profile))
        return motifs


    def GreedyMotifSearchWPsuedocounts(Dna, k, t):
        BestMotifs = []
        for i in range(0, t):
            BestMotifs.append(Dna[i][0:k])

        n = len(Dna[0])
        for i in range(n - k + 1):
            Motifs = []
            Motifs.append(Dna[0][i:i + k])
            for j in range(1, t):
                P = ProfileWithPseudocounts(Motifs[0:j])
                Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
            if (Score(Motifs) < Score(BestMotifs)):
                BestMotifs = Motifs

        print(BestMotifs)
        return Score(BestMotifs)


    def ProfileWithPseudocounts(Motifs):
        profile = {}
        t = len(Motifs)
        k = len(Motifs[0])
        CountMotifs = CountWithPseudocounts(Motifs)
        #print(CountMotifs)
        for symbol in 'ACGT':
            profile[symbol] = []

        for x in CountMotifs:
            for y in CountMotifs[x]:
                z = y / float(t + 4)
                profile[x].append(z)
        #print(profile)
        return profile


    def CountWithPseudocounts(Motifs):
        count = {}
        Pseudocounts = {}
        t = len(Motifs)
        k = len(Motifs[0])

        for symbol in 'ACGT':
            count[symbol] = []
            for j in range(k):
                count[symbol].append(0)

        for i in range(t):
            for j in range(k):
                symbol = Motifs[i][j]
                count[symbol][j] += 1

        for symbol in "ACGT":
            Pseudocounts[symbol] = []

        for x in count:
            for y in count[x]:
                z = y + 1
                Pseudocounts[x].append(z)

        return Pseudocounts


    def ProfileWithMostProbablePattern(Text, k, Profile):
        mostprobval = 0
        for i in range(len(Text) - k + 1):
            kmer = Text[i:i + k]
            probkmerval = Pr(kmer, Profile)
            if probkmerval > mostprobval:
                mostprobval = probkmerval
                mostprobkmer = kmer

        return mostprobkmer


    def Pr(Text, Profile):
        p = 1
        for i in range(len(Text)):
            p = p * Profile[Text[i]][i]

        return p


    def Score(Motifs):
        count = 0
        profile = ProfileWithPseudocounts(Motifs)
        entropy = 0
        k = len(Motifs[0])
        t = len(Motifs)
        ConsensusMotif = Consensus(Motifs)
        for i in range(t):
            for j in range(k):
                if Motifs[i][j] != ConsensusMotif[j]:
                    count += 1
        for symbol in "ACGT":
            for i in range(k):
                prob = profile[symbol][i]
                entropy += -(prob * math.log(prob, 2))

        return count


    def Consensus(Motifs):
        k = len(Motifs[0])
        count = Count(Motifs)

        consensus = ''
        for j in range(k):
            m = 0
            frequentSymbol = ''
            for symbol in 'ACGT':
                if count[symbol][j] > m:
                    m = count[symbol][j]
                    frequentSymbol = symbol
            consensus += frequentSymbol

        return consensus


    def Profile(Motifs):
        profile = {}
        t = len(Motifs)
        k = len(Motifs[0])
        CountMotifs = Count(Motifs)

        for symbol in 'ACGT':
            profile[symbol] = []

        for x in CountMotifs:
            for y in CountMotifs[x]:
                z = y / float(t)
                profile[x].append(z)

        return profile


    def Count(Motifs):
        count = {}
        k = len(Motifs[0])

        for symbol in "ACGT":
            count[symbol] = []
            for j in range(k):
                count[symbol].append(0)

        t = len(Motifs)
        for i in range(t):
            for j in range(k):
                symbol = Motifs[i][j]
                count[symbol][j] += 1

        return count


    def RepeatedRandomizedMotifSearch(Dna, k, t):
        BestScore = float('inf')
        BestMotifs = []
        for i in range(1000):
            Motifs = RandomizedMotifSearch(Dna, k, t)
            CurrScore = Score(Motifs)
            if CurrScore < BestScore:
                BestScore = CurrScore
                BestMotifs = Motifs

        return BestMotifs


    Dna = ['ATGAGGTC',
           'GCCCTAGA',
           'AAATAGAT',
           'TTGTGCTA']

    motifs = ['GTC',
              'CCC',
              'ATA',
              'GCT']
    ans=ProfileWithPseudocounts(motifs)
    print(ans)

    ans2=Motifs(ans, Dna)
    print(ans2)