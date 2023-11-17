class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_count = [0] * 121  
        total_requests = 0


        for age in ages:
            age_count[age] += 1
            
        for age_x in range(1, 121):
            count_x = age_count[age_x]
            for age_y in range(1, 121):
                count_y = age_count[age_y]

                if age_y <= 0.5 * age_x + 7 or age_y > age_x or (age_y > 100 and age_x < 100):
                    continue

                total_requests += count_x * count_y

                if age_x == age_y:
                    total_requests -= count_x

        return total_requests