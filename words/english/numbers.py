import re
def removenumber(text):
    result=re.sub(r'\d+', '',text)
    return result
input_str=" 5 balls are here"
print(removenumber(input_str))
