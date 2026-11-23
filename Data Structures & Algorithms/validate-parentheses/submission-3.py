class Solution:
    def isValid(self, s: str) -> bool:
        
        #
        # Open Brackets => Push to the stack
        # Closed Brackets => Pop from the stack
        #
        # LIFO (Last In First Out)
        #
        # (({})())
        #
        # []
        #
        # Each step we need to ensure that there is a corresponding closing bracket at the top of the stack

        stack = []
        
        for s_i in s:
            print(stack)
            if s_i == '(' or s_i == '{' or s_i == "[":
                stack.append(s_i)
            else:
                if len(stack) == 0:
                    return False
                    
                top = stack.pop()
                if not ((s_i == ')' and top == '(')
                    or (s_i == '}' and top == '{')
                    or (s_i == ']' and top == '[')):
                    return False

        return len(stack) == 0
