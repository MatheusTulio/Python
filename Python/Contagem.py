import re

def printDict(d):
	for key in d:
		print key , ": " , d[key] 

def main():
	with open("README.txt", "r") as arq:
		lista = re.findall(r"[\w']+", arq.read())
		Contagem = {}
		for i in lista:
			if i in Contagem:
				Contagem[i] += 1
			else:
				Contagem[i] = 1
		printDict(Contagem)


main()

