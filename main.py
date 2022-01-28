import re#regex, lets you find only the seven letter words
word_list = list()#defines the word_list varible as a blank list
with open('hello.txt') as f:#fetches words from the hello.txt file
    for line in f.readlines():
        word_list += re.findall(r'\b(\w{7})\b', line)#note the 7, this is filters out all non-7 letter words.
print(word_list[int(len(word_list)/2+2)])#prints word-list but devides this by 2 and then adds 2 bc for some reason this is 2 off aparently:(