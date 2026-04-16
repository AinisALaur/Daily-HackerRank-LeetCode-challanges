class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort()
        stack = []

        for car in cars:
            while len(stack) > 0 and (target - stack[-1][0]) / stack[-1][1] <= (target - car[0]) / car[1]:
                stack.pop()

            stack.append(car)

        return len(stack)


sol = Solution()
print(sol.carFleet(10, [4,1,0,7], [2,2,1,1]))