class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        pos_spe = []
        for i in range(n):
            pos_spe.append([position[i], speed[i]])
        pos_spe = sorted(pos_spe, key= lambda x:x[0] , reverse=True)
        
        for j in range(n):
            time = (target - pos_spe[j][0]) / pos_spe[j][1]
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)