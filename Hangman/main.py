lives=10
hiddenwordlist=[]
word=input("Moderator: Please enter a word. ")
for i in word:
  hiddenwordlist.append("_")
print(*hiddenwordlist)

while True:
  if "_" not in hiddenwordlist:
    print("You win. Congratulations.")
    exit()
  penalty=0
  guess=input("Player: Please enter a guess. ")
  for i in range(len(word)):
    if guess in word[i]:
      penalty=penalty+1
      print("Found it!")
      hiddenwordlist[i]=guess
  print(*hiddenwordlist)

  if penalty==0:
    lives=lives-1
    print(f"Wrong! You have {lives} lives remaining.")
    if lives==0:
      print("You are a useless failiure, game over.")
      exit()