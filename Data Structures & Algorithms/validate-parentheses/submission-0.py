class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "[{(":
                stack.append(i)
            
            elif len(stack) != 0:
                match i:
                    case "]":
                        if stack[-1] != "[":
                            return False
                        else:
                            stack.pop()
                    case ")":
                        if stack[-1] != "(":
                            return False
                        else:
                            stack.pop()
                    case "}":
                        if stack[-1] != "{":
                            return False
                        else:
                                stack.pop()
            else:
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False