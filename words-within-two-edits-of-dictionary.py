from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
   
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]
        node.is_end = True
    
    def dfs(self, query, i, node, changes_made):
        if not node or changes_made > 2:
            return False
        
        if i == len(query):
            return node.is_end

        curr_c = query[i]
        possible = False

        if curr_c in node.children:
            possible = possible or self.dfs(query, i + 1, node.children[curr_c], changes_made)
        
        if changes_made < 2:
            for child in node.children.values():
                possible = possible or self.dfs(query, i + 1, child, changes_made + 1)

        return possible

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        for w in dictionary:
            self.insert(w)

        res = []
        for query in queries:
            if self.dfs(query, 0, self.root, 0):
                res.append(query)
        
        return res
       
solution = Solution()
assert(solution.twoEditWords(queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]) == ["word","note","wood"])
assert(solution.twoEditWords(queries = ["yes"], dictionary = ["not"]) == [])
assert(solution.twoEditWords(queries = ["prfturjd","iarapqqk","aokbrtmx","yafmjorj","larakqqk","nliynmpm","isikkcws","laraeqqk"], dictionary = ["apahhijt","larapqqk","isukkcws","siqqoacj","nloynmpm"]) == ["iarapqqk","larakqqk","nliynmpm","isikkcws","laraeqqk"])