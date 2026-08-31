class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        k = 0
        left = 0
        right = len(people) - 1
        
        while left <= right:
            # If the lightest and heaviest person can fit in the same boat
            if people[left] + people[right] <= limit:
                left += 1
            
            # The heaviest person always gets on a boat (either alone or with the lightest)
            right -= 1
            k += 1
            
        return k