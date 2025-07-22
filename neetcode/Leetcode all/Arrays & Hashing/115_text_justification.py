class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []             # Final list to hold all justified lines
        line, length = [], 0    # 'line' holds current words; 'length' is total chars (excluding spaces)
        i = 0                   # Pointer to current word in words list

        while i < len(words):
            # Check if adding the current word will exceed the line width
            # len(line) is number of gaps (spaces) between words already in line
            if length + len(line) + len(words[i]) > maxWidth:
                # Calculate how much extra space we need to fill
                extra_space = maxWidth - length  # spaces needed to fill the line
                num_gaps = max(1, len(line) - 1) # number of gaps to distribute spaces
                space = extra_space // num_gaps  # evenly distributed spaces per gap
                remainder = extra_space % num_gaps  # some gaps get an extra space

                # Distribute spaces between words
                for j in range(num_gaps):
                    line[j] += " " * space       # Add base number of spaces
                    if remainder > 0:
                        line[j] += " "           # Add one more if we have remainder
                        remainder -= 1

                result.append("".join(line))     # Join the words into a justified line
                line, length = [], 0             # Reset for the next line

            # Add current word to line
            line.append(words[i])
            length += len(words[i])             # Update length of characters (no spaces)
            i += 1

        # Handle the last line — left-justified (no space distribution)
        last_line = " ".join(line)               # Join words with a single space
        trail_space = maxWidth - len(last_line)  # Pad extra spaces at the end
        result.append(last_line + " " * trail_space)

        return result
