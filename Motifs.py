"""
	Añadir las referencias donde se obtuvo la informacion.
	Añadir nombres de referencia 
"""

class Motifs(object):

	HM = [
		1.0,	# 41, 	#Ala -> A 	-> 0
		0.2,	# 49, 	#Cys -> C 	-> 1
		-3.0,	# -55,	#Asp -> D 	-> 2
		-2.6,	# -31,	#Glu -> E 	-> 3
		2.5,	# 100,	#Phe -> F 	-> 4
		0.7,	# 0,	#Gly -> G 	-> 5
		-1.7,	# 8, 	#His -> H 	-> 6
		3.1,	# 99, 	#Ile -> I 	-> 7
		-4.6,	# -23,	#Lys -> K 	-> 8
		2.2,	# 97, 	#Leu -> L 	-> 9
		1.1,	# 74, 	#Met -> M 	-> 10
		-2.7,	# -28,	#Asn -> N 	-> 11
		-0.3,	# -46,	#Pro -> P 	-> 12
		-2.9,	# -10,	#Gln -> Q 	-> 13
		-7.5,	# -14 	#Arg -> R 	-> 14
		-1.1,	# -5, 	#Ser -> S 	-> 15
		-0.8,	# 13, 	#Thr -> T 	-> 16
		2.3,	# 76, 	#Val -> V 	-> 17
		1.5,	# 97, 	#Trp -> W 	-> 18
		0.1,	# 63, 	#Tyr -> Y 	-> 19
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
		071.0779, # 089.09, #Ala -> A
		103.1429, # 121.16, #Cys -> C 
		115.0874, # 133.10, #Asp -> D
		129.1140, # 147.13, #Glu -> E
		147.1739, # 165.19, #Phe -> F 
		057.0513, # 075.07, #Gly -> G
		137.1393, # 155.15, #His -> H
		113.1576, # 131.17, #Ile -> I
		128.1723, # 146.19, #Lys -> K
		113.1576, # 131.17, #Leu -> L
		131.1961, # 149.21, #Met -> M
		114.1026, # 132.12, #Asn -> N 
		097.1152, # 115.13, #Pro -> P
		128.1292, # 146.14, #Gln -> Q 
		156.1857, # 0174.20, #Arg -> R
		087.0773, # 105.09, #Ser -> S
		101.1039, # 119.12, #Thr -> T
		099.1311,# 119.15, #Val -> V
		186.2099,# 204.23, #Trp -> W
		163.1733# 181.19 #Tyr -> Y
		# Referencia http://www.matrixscience.com/help/aa_help.html.
	]	

	# Funcion con la que se general la matriz de HCI
	def generaHCI(self,A,B):
		hci = 20 - abs(((self.HM[A]-self.HM[B])*19)/10.6)
		return hci

	# Funcion con la que se general la matriz de CCI
	def generaCCI(self,A,B):
		cci = 11 - (((self.pl[A]-7)*(self.pl[B]-7)*19)/33.8)
		return cci

	# Funcion con la que se general la matriz de SCI
	def generaSCI(self,A,B):
		sci = 20 - abs((((self.MW[A]+self.MW[B])-118.4825)*19)/253.9373)# 253.9373 -> RW )
		return sci 

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

		for x in range(20):
			aux1 = []
			aux2 = []
			aux3 = []
			for y in range(20):
				aux1.append(self.generaSCI(x,y))
				aux2.append(self.generaCCI(x,y))
				aux3.append(self.generaHCI(x,y))
				pass
			self.SCIM.append(aux1)
			self.CCIM.append(aux2)
			self.HCIM.append(aux3)
			pass

	# Funcion que devuelve las matrices guia. 
	def SCICCIHCI(self):

		self.HCIM = []
		self.CCIM = []
		self.SCIM = []

		for x in range(20):
			aux1 = []
			aux2 = []
			aux3 = []
			for y in range(20):
				aux1.append(self.generaSCI(x,y))
				aux2.append(self.generaCCI(x,y))
				aux3.append(self.generaHCI(x,y))
				pass
			self.SCIM.append(aux1)
			self.CCIM.append(aux2)
			self.HCIM.append(aux3)
			pass
		return self.SCIM,self.CCIM,self.HCIM

