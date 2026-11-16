class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def get_next_number(n):
            output = 0
            while n:
                output += (n%10)**2
                n = n // 10
            return output

        slow = get_next_number(n)
        fast = get_next_number(get_next_number(n))

        while slow != fast:
            if fast == 1: return True
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))
        
        return slow == 1
        
        

        
        