from typing import List
from collections import deque
startGene = "ATGC"
endGene = "AACC"
bank = ["TACC", "ACGC", "TCGT", "ACGT", "AAGT","AAGA","AACA","AACC", "AAAA"]
bank = ["TACC", "ACGC", "ACCC", "ACGT", "AAGT","AAGA","AACA","AACC", "AAAA"]
# startGene = "AAC"
# endGene = "CCC"
# # bank = ["TACC", "ACGC", "TCGT", "ACGT", "AAGT","AAGA","AACA","AACC", "AAAA"]
# bank = ["TACC", "ACGC", "ACCC", "ACGT", "AAGT","AAGA","AACA","AACC", "AAAA"]
# bank = ["AAA","AAC","ACC","CCC","ACA","CCA"]
# # bank = ["AA","AAC","ACC","CCC","ACA","CCA"]


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        self.endGene = endGene
        self.min_chain = []
        self.getNextM(startGene, [], set(bank))
        if self.min_chain == []:
            return -1
        else:
            return len(self.min_chain) - 1

    def getNextM(self, gene,  current_chain, bank):
        current_chain.append(gene)
        diff = []
        temp_set = set()
        for i in range(len(self.endGene)):
            temp_set.update(tuple([gene[:i] + e + gene[i+1:] for e in "ACGT"]))
        temp_set = bank.intersection(temp_set)
        if len(temp_set)==0:
            return
        if self.endGene in temp_set:
            current_chain.append(self.endGene)
            if len(self.min_chain) == 0:
                self.min_chain = current_chain
            if len(current_chain) < len(self.min_chain):
                self.min_chain = current_chain
        else:
            for gene in temp_set:
                bank = bank.difference({gene})
                self.getNextM(gene, current_chain[:], bank)
                bank = bank.union({gene})

s = Solution()
print(s.minMutation(startGene, endGene, bank))
print(s.min_chain)


class Solution2:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        mutations = deque()
        verified = [startGene]
        mutations.append(startGene)
        mutation_chains = {startGene: None}
        self.min_chain = []
        bank = set(bank)
        while len(mutations) > 0:
            current_mutation = mutations.popleft()
            temp_set = set()
            for i in range(len(current_mutation)):
                temp_set.update(tuple([current_mutation[:i] + e + current_mutation[i+1:] for e in "ACGT"]))
            temp_set = bank.intersection(temp_set)
            if len(temp_set)==0:
                continue
            if endGene in temp_set:
                mutation_chain = deque()
                mutation_chain.appendleft(endGene)
                mutation_chain.appendleft(current_mutation)
                node = mutation_chains[current_mutation]
                while node != None:
                    mutation_chain.appendleft(node)
                    node = mutation_chains[node]
                if len(self.min_chain) == 0:
                    self.min_chain = mutation_chain.copy()
                if len(mutation_chain) < len(self.min_chain):
                    self.min_chain = mutation_chain.copy()
            else:
                for gene in temp_set:
                    if not gene in verified:
                        mutations.append(gene)
                        verified.append(gene)
                        mutation_chains[gene] = current_mutation
        return len(self.min_chain)-1 if len(self.min_chain)>0 else -1


s = Solution()
print(s.minMutation(startGene, endGene, bank))