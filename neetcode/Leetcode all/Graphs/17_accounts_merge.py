from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)

        # Maps each email to a unique integer index
        emailIdx = {}  # email -> id
        # Stores all emails in order (so we can map id -> email later)
        emails = []
        # Maps each email index back to the account id it first appeared in
        emailToAcc = {}  # email_index -> account_Id

        m = 0  # counter for assigning unique ids to emails
        for accId, a in enumerate(accounts):       # go through each account
            for i in range(1, len(a)):            # skip the name (a[0])
                email = a[i]
                if email in emailIdx:             # if email already seen, skip
                    continue
                emails.append(email)              # store email string
                emailIdx[email] = m               # assign unique index
                emailToAcc[m] = accId             # map email index -> account id
                m += 1

        # Build adjacency list graph for emails (m unique emails total)
        adj = [[] for _ in range(m)]
        for a in accounts:
            # connect consecutive emails in the same account
            for i in range(2, len(a)):
                id1 = emailIdx[a[i]]
                id2 = emailIdx[a[i - 1]]
                adj[id1].append(id2)
                adj[id2].append(id1)

        # emailGroup[accId] = list of merged emails for this account
        emailGroup = defaultdict(list)
        # Track visited emails during DFS
        visited = [False] * m

        # Depth-first search to collect all connected emails
        def dfs(node, accId):
            visited[node] = True
            emailGroup[accId].append(emails[node])   # store email string
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, accId)

        # Traverse each email id, run DFS for unvisited ones
        for i in range(m):
            if not visited[i]:
                dfs(i, emailToAcc[i])

        res = []
        # Construct final merged accounts result
        for accId in emailGroup:
            name = accounts[accId][0]  # account name (first element)
            # Sort emails for lexicographic order
            res.append([name] + sorted(emailGroup[accId]))

        return res
