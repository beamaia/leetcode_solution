class Solution:
    
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0]:
            return False
        
        if len(name) > len(typed):
            return False
        
        prev = name[0]
        letters = list(typed)
        letters.pop(0)
        
        index_name = 1
        name_size = len(name) - 1
        
        for i in range(1, len(typed)):
            if index_name > name_size:
                break
            if name[index_name] == typed[i]:
                prev = name[index_name]
                index_name += 1
                letters.pop(0)
            elif prev == typed[i]:
                letters.pop(0)
            else:
                return False
        
        if len(letters):
            iter_ = 0
            while len(letters) > iter_:
                if letters[iter_] != name[-1]:
                    return False
                iter_ += 1
            
            return True
        if not len(letters) and index_name > name_size:
            return True
        return False