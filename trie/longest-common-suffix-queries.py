class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.idx = float("inf")
        self.min_len = float("inf")


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        root = TrieNode()
        res = []

        for i, word in enumerate(wordsContainer):
            node = root

            if len(word) < node.min_len:
                node.min_len = len(word)
                node.idx = i

            for ch in reversed(word):
                node = node.children[ch]
                if len(word) < node.min_len:
                    node.idx = i
                    node.min_len = len(word)

        for word in wordsQuery:
            node = root

            for ch in reversed(word):
                if ch in node.children:
                    node = node.children[ch]
                else:
                    break

            res.append(node.idx)

        return res
