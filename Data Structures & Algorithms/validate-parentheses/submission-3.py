class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inHash = {")": "(", "]":"[", "}": "{"}

        for i in s:
            if i in inHash:
                if stack and stack[-1] == inHash[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False