s = input('Give me a string = ')
s_free = s.replace('.',' ').replace(',',' ')
s_free = s_free.replace('!',' ').replace('?',' ')

words = s_free.split()

feature = ('word','length')
width=[10,6]

width_word = width[0]
width_len = width[1]

form_hline = '+'+'-'*width_word+'+'+'-'*width_len+'+'
form_title = "|%{0}s|%{1}s|".format(width_word,width_len)
form_word = "|%{0}s|%{1}s|".format(width_word, width_len)

print(form_hline)
print(form_title % feature)
print(form_hline)

for wd in words:
 print(form_word % (wd, len(wd)))
 print(form_hline)