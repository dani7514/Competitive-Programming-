class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack=[{}]
        i=0
        while i< len(formula):
            if formula[i] == '(' :
                stack.append({})
                i+=1
            elif formula[i] == ')':
                popStack=stack.pop()
                
                i+=1
                nextIndex= i
                while i < len(formula) and formula[i].isdigit():
                    i+=1
                    
                multiplayer=0
                if (formula[nextIndex:i]):
                    multiplayer=int(formula[nextIndex:i])
                else:
                    multiplayer=1
                
                for j in popStack:
                    if (j in stack[-1]):
                        stack[-1][j] += (popStack[j]* multiplayer)
                    else:
                        stack[-1][j] = (popStack[j]* multiplayer)
            else:
                c=formula[i]
                i+=1
                start=i
                while i < len(formula) and formula[i].islower():
                    i+=1
                c+=formula[start:i]
                
                nex= i
                while i < len(formula) and formula[i].isdigit():
                    i+=1
                    
                count=0
                if (formula[nex:i]):
                    count=int(formula[nex:i])
                else:
                    count=1
                    
                if (c in stack[-1]):
                    stack[-1][c]+=count
                else:
                    stack[-1][c]=count
                
        result=''
        temp=stack[-1]
        sortedD=sorted(temp.items())
          
        for (k,r) in sortedD:
            result=result+k
            if (r>1):
                result+=str(r)
        return result
            
        
                
                
                
                
        
                
                
                
                