print('Implementation of vignere cipher method as python')

# keyw func
def genKey(string, emilia):
	emilia = list(emilia)
	if len(string) == len(emilia):
		return(emilia)
	else:
		for i in range(len(string) -
			len(emilia)):
			emilia.append(emilia[i % len(emilia)])
	return("" . join(emilia))

# enc func
def akenoH(string, key):
	ilya = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A')
		ilya.append(chr(x))
	return("" . join(ilya))

# dec func
def eruC(ilya, key):
	aseli = []
	for i in range(len(ilya)):
		x = (ord(ilya[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		aseli.append(chr(x))
	return("" . join(aseli))

# calling n run dude
if __name__ == "__main__":
	string = input('Input a text : ')
	keyword = input('Input keyword : ')
	koendji = genKey(string, keyword)
	ciphT = akenoH(string,koendji)
	print("Encrypted :", ciphT)
	print("Decrypted :", eruC(ciphT, koendji))
