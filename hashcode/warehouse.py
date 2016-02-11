#Structure WareHouse

class WareHouse:
	#listeProduit, si il y a deux produits de types 100 : [100,100]
	def __init__(self, listeCoord, listeProduit):
		self.coord = listeCoord
		self.produits = listeProduit
	
