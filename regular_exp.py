# Q1:-  Extract the user id, domain name and suffix from the following email addresses.
'''
import re
emails = ["zuck26@facebook.com","page33@google.com","jeff42@amazon.com"]
output=[]
for i in emails:
    output.append(tuple(re.split('[@.]',i)))
print(output)
'''

# Q2:- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
'''
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
output=re.findall('[bB]\S*',text)
print(output)
'''

# Q3:- Split the following irregular sentence into words.
'''
import re
sentence="A,very very; irregular_sentence"
output=re.sub('[\W_]',' ',sentence)
print(output)
'''

# Q4:-  Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
'''
p= "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today... http://t.co/lbwej0pxOd cc: @garybernhardt #rstats" 
p=p.replace("http://t.co/lbwej0pxOd cc: @garybernhardt #rstats","")
q=(p)
q=q.replace("! RT @TheNextWeb:","")
print(q)
'''
