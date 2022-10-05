str = input("Give a string = ")
wd = input("Give a word = ")
sentence = str.strip()

n = len(sentence)
m = len(sentence.replace(wd,""))
print("What is the number of [{0}] in [{1}] ?".format(wd,sentence))
print("The answer is {0}.".format(int((n-m)/len(wd))))