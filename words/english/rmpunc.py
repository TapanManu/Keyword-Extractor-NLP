import re
def rmpunctuation(text):
    result=re.sub('[^a-zA-Z]',' ',text)
    return result
input_str=" come,let's go for a walk"
print(rmpunctuation(input_str))
