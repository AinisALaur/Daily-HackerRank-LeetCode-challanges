class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        count = 0
        i = 0
        j = len(people) - 1
        people.sort()

        while i <= j:
            if i == j:
                count += 1
                break

            if people[i] + people[j] > limit:
                j -= 1
                count += 1            
            
            else:
                count += 1
                i += 1
                j -= 1

        return count
            
            
sol = Solution()
people = [5,1,4,2]
limit = 6
print(sol.numRescueBoats(people, limit))