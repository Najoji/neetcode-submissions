class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {}
        stack= []
        for i in range(len(position)):
            cars[position[i]] = speed[i]
        
        for i in sorted(cars.keys() , reverse = True ):
            s = cars[i]

            stack.append((target - i) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

        


        