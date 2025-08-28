from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                L = len(words[i])
                if words[i] == words[j][:L] and words[i] == words[j][-L:]:
                    result += 1
        
        return result
    
# TRIE

# Each TrieNode represents a node in the Trie
class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes
        # Key = tuple of (prefix character, suffix character)
        # Value = another TrieNode
        self.children = {}
        
        # Count of how many words pass through this node
        self.count = 0


# Trie data structure to handle prefix-suffix matching
class Trie:
    def __init__(self):
        # Root node of the Trie
        self.root = TrieNode()
    
    # Add a word into the Trie
    def add(self, w):
        cur = self.root  # Start from root node

        # Pair each character with the corresponding reversed character
        # Example: word = "abc"
        # zip("abc", "cba") → (a,c), (b,b), (c,a)
        for c1, c2 in zip(w, reversed(w)):
            # If this pair is not yet in children, create a new TrieNode
            if (c1, c2) not in cur.children:
                cur.children[(c1, c2)] = TrieNode()
            
            # Move to the child node for this pair
            cur = cur.children[(c1, c2)]
            
            # Increment count (tracking how many words share this prefix-suffix pair path)
            cur.count += 1
    
    # Count how many words already in Trie share the same prefix-suffix pattern as word `w`
    def count(self, w):
        cur = self.root

        # Walk down the Trie in the same (prefix, suffix) order
        for c1, c2 in zip(w, reversed(w)):
            # If this pair is not found, no word matches → return 0
            if (c1, c2) not in cur.children:
                return 0
            
            # Otherwise, move deeper
            cur = cur.children[(c1, c2)]
        
        # Return how many words share this exact (prefix-suffix) traversal
        return cur.count


# Main solution class
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        root = Trie()  # Create an empty Trie

        # Traverse the words list in reverse order
        for w in reversed(words):
            # Count how many previous words (to the right in original order)
            # share prefix & suffix structure with current word
            result += root.count(w)

            # Then add current word into the Trie
            root.add(w)
        
        # Final result = total number of prefix-suffix pairs
        return result
