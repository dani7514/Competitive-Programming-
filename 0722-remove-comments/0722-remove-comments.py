class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        is_inBlock = False
        line = ""
        
        for s in source:
            i = 0
            while i < len(s):
                if is_inBlock:
                    if s[i:i+2] == "*/":
                        is_inBlock = False
                        i += 1  
                else:
                    if s[i:i+2] == "//":
                        break
                    elif s[i:i+2] == "/*":
                        is_inBlock = True
                        i += 1  
                    else:
                        line += s[i]
                i += 1

            if line and not is_inBlock:
                result.append(line)
                line = ""

        return result
                      
                                         
                                         
                            
                                
                        
                        
                            
                                
                                
                                
                            
                    
            
            
        
        