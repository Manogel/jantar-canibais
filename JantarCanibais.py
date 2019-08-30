import time 
from threading import Thread

class semaforo: 
	controle = True #Controle o fluxo de canibais, funciona como um juíz  

#Tirar a Thread de Cozinheiro
class Cozinheiro: 
	controle = False #Variável que indica se o cozinheiro está acordado 
	def encher():
		print('Caldeirão vazio')
		time.sleep(1)
		print('Cozinheiro enchendo o caldeirão')
		time.sleep(7)
		print('Cozinheiro terminou de encher o caldeirão e foi dormir!')
		caldeirão.quantidade = 10


class caldeirão: 
	quantidade= 0


class Canibal(Thread):
	def __init__(self, num):
		Thread.__init__(self)
		self.num = num
		
	def run(self):
		
		while True:
			if semaforo.controle:
				semaforo.controle = False
				if caldeirão.quantidade!=0: 
					print('Canibal {} servindo'.format(self.num))
					time.sleep(2)
					print('Canibal {} terminou de servir'.format(self.num))
					semaforo.controle = True
					caldeirão.quantidade-=1
					print(f'Canibal {self.num} comendo')
					time.sleep(3)
				else:
					print(f'Canibal {self.num} dormindo') 
					Cozinheiro.encher()
					semaforo.controle = True

""" cozinheiro = Cozinheiro()
cozinheiro.start() """

c = Canibal('Lucas')
c.start()
c = Canibal('Manoel')
c.start()
c = Canibal('Alender')
c.start()
c = Canibal('Paulo')
c.start()
c = Canibal('Gustavo')
c.start()