class Solution:
    def interpret(self, command: str) -> str:
        st = ""
        i=0
        while i<len(command):
            if command[i]=="G":
                st+="G"
                i+=1
            elif command[i]=="(":
                i+=1
            elif command[i]=="a":
                st+="al"
                i+=3
            else:
                st+="o"
                i+=1
        return st
            

                
                    
                