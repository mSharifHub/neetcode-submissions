class Solution:
    def calPoints(self, operations: List[str]) -> int:
    
        record = []

        for current in operations:
            if current == 'C':
                if len(record) >= 1:
                    record.pop()

            elif current == '+':
                if len(record) >= 2:
                    prior_two = record[-1] + record[-2]
                    record.append(prior_two)
            elif current == 'D':
                if len(record) >=1:
                    prior = record[-1] * 2
                    record.append(prior)
            else:
                record.append(int(current))

        result = sum(record)
        return result
                                                    

 


        
            
                
            
        