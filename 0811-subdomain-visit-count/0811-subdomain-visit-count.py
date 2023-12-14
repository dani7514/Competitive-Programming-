class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_dict = {}
        
        for index in range(len(cpdomains)):
            split_num_to_domain = cpdomains[index].split(' ')
            num = int(split_num_to_domain[0])
            domain = split_num_to_domain[1]
            
            if domain in domain_dict:
                domain_dict[domain] += num
            else:
                 domain_dict[domain] = num
            
            for index_domain in range(len(domain)):
                if domain[index_domain] == "." :
                    temp = domain[index_domain + 1: ]
                    if temp in domain_dict:
                        domain_dict[temp] += num
                    else:
                         domain_dict[temp] = num               
        
        result = []
        for domain in domain_dict:
            result.append(str(domain_dict[domain]) + " " + domain)
            
        return result