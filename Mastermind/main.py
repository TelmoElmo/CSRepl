code=input("Moderator: Please enter a 4-digit code:\n")
guess=input("Player: Please enter your 4-digit guess:\n\n")
num=0
while guess!=code:
  guess2=guess
  code2=code
  answer=[]
  for i in range(4):
    if guess2[i]==code2[i]:
      answer.append('b')
      code2=code2.replace(code2[i],"£",1)
      guess2=guess2.replace(guess2[i],"£",1)

  for i in range (4):
    if guess2[i] in code2:
      if guess2[i].isnumeric()==True:
        answer.append('w')
        code2=code2.replace(guess2[i],"£",1)
        guess2=guess2.replace(guess2[i],"£",1)

  print(*answer)
  num+=1
  if num<10:
    guess=input(f"{10-num} guesses; try again\n\n")
  else:
    break
if num<10:
  print("You win!")
else:
  print("You lost :(")
#I'm a genius btw