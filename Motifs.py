

class Motifs(object):

	HM = [
		1.0,	# 41, 	#Ala -> A 	-> 1
		0.2,	# 49, 	#Cys -> C 	-> 2
		-3.0,	# -55,	#Asp -> D 	-> 3
		-2.6,	# -31,	#Glu -> E 	-> 4
		2.5,	# 100,	#Phe -> F 	-> 5
		0.7,	# 0,	#Gly -> G 	-> 6
		-1.7,	# 8, 	#His -> H 	-> 7
		3.1,	# 99, 	#Ile -> I 	-> 8
		-4.6,	# -23,	#Lys -> K 	-> 9
		2.2,	# 97, 	#Leu -> L 	-> 10
		1.1,	# 74, 	#Met -> M 	-> 11
		-2.7,	# -28,	#Asn -> N 	-> 12
		-0.3,	# -46,	#Pro -> P 	-> 13
		-2.9,	# -10,	#Gln -> Q 	-> 14
		-7.5,	# -14 	#Arg -> R 	-> 15
		-1.1,	# -5, 	#Ser -> S 	-> 16
		-0.8,	# 13, 	#Thr -> T 	-> 17
		2.3,	# 76, 	#Val -> V 	-> 18
		1.5,	# 97, 	#Trp -> W 	-> 19
		0.1,	# 63, 	#Tyr -> Y 	-> 20
	]

	pl = [
		6.00, #Ala -> A
		5.07, #Cys -> C
		2.77, #Asp -> D
		3.22, #Glu -> E
		5.48, #Phe -> F
		5.97, #Gly -> G
		7.59, #His -> H
		6.02, #Ile -> I
		9.74, #Lys -> K
		5.98, #Leu -> L
		5.74, #Met -> M
		5.41, #Asn -> N
		6.30, #Pro -> P
		5.65, #Gln -> Q
		10.76, #Arg -> R
		5.68, #Ser -> S
		5.60, #Thr -> T
		5.96, #Val -> V
		5.89, #Trp -> W
		5.66, #Tyr -> Y
	]

	MW = [
		089.09, #Ala -> A
		121.16, #Cys -> C 
		133.10, #Asp -> D
		147.13, #Glu -> E
		165.19, #Phe -> F 
		075.07, #Gly -> G
		155.15, #His -> H
		131.17, #Ile -> I
		146.19, #Lys -> K
		131.17, #Leu -> L
		149.21, #Met -> M
		132.12, #Asn -> N 
		115.13, #Pro -> P
		146.14, #Gln -> Q 
		0174.20, #Arg -> R
		105.09, #Ser -> S
		119.12, #Thr -> T
		119.15, #Val -> V
		204.23, #Trp -> W
		181.19 #Tyr -> Y
	]	

	# Funcion con la que se general la matriz de HCI
	def generaHCI(self,A,B):
		hci = 20 - abs((self.HM[A]-self.HM[B])*(19/10.6))
		return hci
		pass

	# Funcion con la que se general la matriz de CCI
	def generaCCI(self,A,B):
		cci = 11 - ((self.pl[A]-7)*(self.pl[B]-7)*(19/33.8))
		return cci
		pass

	# Funcion con la que se general la matriz de SCI
	def generaSCI(self,A,B):
		sci = 20 - abs((self.MW[A]+self.MW[B]-123)*(19/135))
		return sci 
		pass

	def imprimeMatrix(self,Matrix):
		for y in Matrix:
			print("[", end="")
			for x in y:
				print('{0:.3f}'.format(x), end=",")
				pass
			print("]")
			pass
		pass

	def __init__(self):

		self.HCIM = []
		self.CCIM = []
		self.SCIM = []

		for x in range(0,20):
			aux1 = []
			aux2 = []
			aux3 = []
			for y in range(0,20):
				aux1.append(self.generaSCI(x,y))
				aux2.append(self.generaCCI(x,y))
				aux3.append(self.generaHCI(x,y))
				pass
			self.SCIM.append(aux1)
			self.CCIM.append(aux2)
			self.HCIM.append(aux3)
			pass