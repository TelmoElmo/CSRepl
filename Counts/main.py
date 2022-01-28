BASE = 36.87
count = 0.0
	 
count = float (input ("Enter a count "))
if count <= 5:
  print(count * BASE)
elif count <= 15:
  print(count * BASE * 0.8)
elif count >= 16:
  print(count * BASE * 0.7)