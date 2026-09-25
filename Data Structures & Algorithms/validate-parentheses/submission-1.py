class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stackhash = {")" : "(", "]":"[", "}": "{"}

        for i in s:
            if i in stackhash:
                if stack and stack[-1] == stackhash[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        