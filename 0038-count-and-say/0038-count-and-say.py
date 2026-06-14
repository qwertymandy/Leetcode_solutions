class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: the first term of the sequence is always "1"
        result = "1"
        
        # Iteratively generate the sequence from the 2nd term up to the nth term
        for _ in range(n - 1):
            next_result = []
            i = 0
            
            # Scan through the current string to group identical consecutive digits
            while i < len(result):
                digit = result[i]
                count = 1
                
                # Count how many times the current digit repeats consecutively
                while i + count < len(result) and result[i + count] == digit:
                    count += 1
                
                # Append the count and the digit to our next sequence builder
                next_result.append(str(count))
                next_result.append(digit)
                
                # Advance the pointer past the processed group
                i += count
                
            # Update the result to the newly formed string sequence
            result = "".join(next_result)
            
        return result
