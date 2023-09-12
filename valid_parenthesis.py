class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(': ')', '[': ']', '{': '}'}
        temp = []
        #edge
        l = len(s)
        if l == 0:
            return True
        if l == 1:
            return False

        for i in s:
            #opening mark
            if i in list(dict.keys()):
                temp.append(i)
            #closing mark
            else:
                if len(temp) == 0: #start with closing
                    return False
                if i == dict[temp[-1]]: #if close existing
                    temp.pop()
                else:
                    return False
        if len(temp) != 0: #any opening not closed
            return False
        return True

            
