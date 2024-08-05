class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        
        for i in details:
            sum = i[11:13]
            
            if int(sum) > 60:
                count += 1
        
        return count