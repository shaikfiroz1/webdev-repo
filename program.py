def anagram (word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    if len(word1) != len(word2):
     return False 


    freq={}
    for char in word1:
     freq[char]= freq.get(char, 0) + 1


    for char in word2 :
      if char  not in freq:
        return False 
      
      freq[char] -= 1

      if freq[char] <0:
         return False
      
    return all(v == 0 for v in freq.values())  
      
print(anagram("firoz", "zofir"))