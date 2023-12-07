class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losser_dict = {}
        
        for i in range(len(matches)):
            if matches[i][1] in losser_dict:
                losser_dict[matches[i][1]] += 1
            else:
                losser_dict[matches[i][1]] = 1
        
        not_loss_anyMatch = []
        
        for i in range(len(matches)):
             if matches[i][0] not in losser_dict and matches[i][0] not in  not_loss_anyMatch :
                not_loss_anyMatch.append(matches[i][0])
        
        lost_exactly_once = []
        
        for i in losser_dict:
            if losser_dict[i] == 1:
                lost_exactly_once.append(i)
                
        not_loss_anyMatch.sort()
        lost_exactly_once.sort()
        
        result = []
        result.append(not_loss_anyMatch)
        result.append(lost_exactly_once)
        
        return result
        