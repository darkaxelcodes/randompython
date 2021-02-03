def isAnagram(str1, str2):
    try:
        str1List = list(str1.lower().replace(' ',''))
        assert(len(str2) == len(str1List))    
        for char in str2.lower().replace(' ',''):
            if char in str1List:
                str1List.remove(char)
        if not str1List:
            return True
        else:
            return False
    except AssertionError:
        print("The two strings are not equal in size!")
        
print(isAnagram("modern", "norman"))
        
        