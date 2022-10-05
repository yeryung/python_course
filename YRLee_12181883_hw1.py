abc = input("Give a string : ")
xyz = abc.strip()
words = xyz.split('.')
print(words)
pre ='['+ words[0] + ']'
post = '[['+ words[1] + ']]'
print(pre)
print(post)