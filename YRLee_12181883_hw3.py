str = input("Give a string = ")

import re
str = str.replace(" ","")
str = re.split('([-|+])', str)
answer = []

# 빈문자열 제거
for s in str:
    if s == '':
        str.remove('')

for i in range(len(str)):
    if 'x' in str[i]:
        s = str[i].split('x^')
        if s[0] == '':
            if str[i-1] == '-':
                s[0] = '-1'
            else:
                s[0] = '1'
        else:
            if str[i-1] == '-':
                s[0] = '-' + s[0]
            
        answer.append((s[0],s[1]))       

print(answer)







