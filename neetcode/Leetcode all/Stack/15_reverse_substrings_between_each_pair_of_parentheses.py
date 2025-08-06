class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ')':
                portion = []
                while stack[-1] != '(':
                    portion.append(stack.pop())
                stack.pop()
                stack.extend(portion)
            else:
                stack.append(c)

        return "".join(stack)
    
class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Step 1: Preprocess to find matching parentheses
        pair = {}  # Dictionary to map opening and closing parentheses
        stack = []  # Stack to keep track of '(' indices

        # First pass: record positions of matching parentheses
        for i, c in enumerate(s):
            if c == "(":  # When we find an opening bracket
                stack.append(i)
            elif c == ")":  # When we find a closing bracket
                j = stack.pop()  # Get the index of the matching opening bracket
                pair[i] = j  # Map closing to opening
                pair[j] = i  # Map opening to closing
        
        # Step 2: Traverse the string using jumping logic with a direction switch
        i, direction = 0, 1  # Start from index 0, going forward (direction = 1)
        result = []  # To build the final output

        while i < len(s):
            if s[i] == "(" or s[i] == ")":
                # Jump to the matching parenthesis and reverse direction
                i = pair[i]
                direction = -direction  # Reverse traversal direction
            else:
                # Append regular characters to result
                result.append(s[i])
            # Move to the next index based on direction (+1 or -1)
            i += direction
        
        return "".join(result)  # Combine characters into a final string
