sentence = 'the cat sat on the mat the cat'
freq = {}
for element in sentence.split():
     freq[element] = freq.get (element , 0) +1 
print (freq)