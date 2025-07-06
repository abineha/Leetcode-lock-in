from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
        # Step 1: Combine the logs and sort by time
        logs = sorted(zip(timestamp, username, website))

        # Step 2: Build each user's ordered website visit list
        user_visits = defaultdict(list)
        for _, user, site in logs:
            user_visits[user].append(site)

        # Step 3: Count how many users have each 3-sequence pattern
        pattern_count = defaultdict(int)
        for user, visits in user_visits.items():
            seen_patterns = set()
            n = len(visits)
            # Generate all 3-sequences for the user's visits
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        pattern = (visits[i], visits[j], visits[k])
                        seen_patterns.add(pattern)
            # Increment count only once per user per pattern
            for pattern in seen_patterns:
                pattern_count[pattern] += 1

        # Step 4: Find the pattern with the highest count (tie-breaker: lexicographically smallest)
        best_pattern = ()
        max_users = 0
        for pattern, count in pattern_count.items():
            if count > max_users or (count == max_users and pattern < best_pattern):
                best_pattern = pattern
                max_users = count

        return list(best_pattern)
