class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        arr = []

        for i in asteroids:
            while len(arr) >= 1 and arr[-1] > 0 and i < 0:
                if abs(arr[-1]) < abs(i):
                    arr.pop()

                elif abs(arr[-1]) == abs(i):
                    arr.pop()
                    break
                
                else:
                    break

            else:
                arr.append(i)

        return arr


sol = Solution()
print(sol.asteroidCollision([2,4,-4,-1]))