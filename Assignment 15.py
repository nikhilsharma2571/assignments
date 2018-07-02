#q1

import re
'''e="zuck26@facebook.com," \
    "page33@google.com," \
    "jeff42@amazon.com"
a=re.split('\W',e)
print(a)'''

#q2

'''text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better"
name=re.findall("[bB][\w]{1,20}",text)
print(name)'''

#q3

'''sentence = "A, very very; irregular_sentence"
a=re.sub('[;,_:]',' ',sentence)
print(a)'''


#q4


tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today'
a=re.sub('[^\w\s]','',tweet)
print(a)