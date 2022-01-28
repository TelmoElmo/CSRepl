win=0
import random

ran=(random.randrange(1, 100))
while win < 1:
  guess=int(input("I'm thinking of a number betwwen 1 & 100. Please guess the number I'm thinking of."))
  if ran==guess:
    win=1
    print("Yes! You guessed it right! Game Over")
  elif ran<guess:
    print("Not quite, you're too high.")
  elif ran>guess:
    print("Not quite, you're too low.")