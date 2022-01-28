alpha = "abcdefghijklmnopqrstuvwxyz"
print(alpha[16])
print(alpha.index("t"))
string=input("Type in your string: ")
string=string.lower()
shift=int(input("How far would you like it shifted?"))
for letter in string:
	num=alpha.index(letter)+shift
	num=num%26
	newletter=alpha[num]
	print(newletter, end="")