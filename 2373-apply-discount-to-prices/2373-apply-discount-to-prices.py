class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words= sentence.split(' ')
        multiplier=(100-discount)/100
        res=[]
        for word in words:
            if word.startswith('$') and word[1:].isdigit():
                price=int(word[1:])
                discounted_price=price*multiplier
                res.append(f"${discounted_price:.2f}")
            else:
                res.append(word)
        return ' '.join(res)


       
    
