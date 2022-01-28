barry=input()
key="IIMCCCW"
for i in range(6):
    if barry[i]==key[i]:
      key=key.replace(key[i],"#",1)
      print(key)