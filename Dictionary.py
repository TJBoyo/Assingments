dic = {}
Text_in = input('Enter a line of text:' )

texts = Text_in.split()

for text in texts:
    dic[text] = dic.get(text, 0) + 1
print(dic)
