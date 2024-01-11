class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        result = []

        if len(firstList) == 0 or len(secondList) == 0:
            return []

        while first < len(firstList) and second < len(secondList):
            temp = set()

            if secondList[second][0] <= firstList[first][0] <=  secondList[second][1]:
                temp.add(firstList[first][0])
            if secondList[second][0] <= firstList[first][1] <=  secondList[second][1]:
                temp.add(firstList[first][1])
            if firstList[first][0] <= secondList[second][0] <=  firstList[first][1]:
                temp.add(secondList[second][0])
            if firstList[first][0] <= secondList[second][1] <=  firstList[first][1]:
                temp.add(secondList[second][1])

            if temp:
                if len(temp) == 1:
                    t = []
                    for i in temp:
                        t.append(i)
                        t.append(i)
                    result.append(t)
                else:
                    temp = sorted(temp)
                    t = []
                    for i in temp:
                        t.append(i)
                    result.append(t)

            if secondList[second][1] < firstList[first][1]:
                second += 1
            elif secondList[second][1] > firstList[first][1]:
                first += 1
            else:
                first += 1
                second += 1

        return result

            