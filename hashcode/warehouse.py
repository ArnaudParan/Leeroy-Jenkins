#Structure WareHouse

class WareHouse:
	#listeProduit, si il y a deux produits de types 100 : [100,100]
	#self.produits est un dictionnaire.
	def __init__(self, listeCoord, listeProduit):
		self.r = listeCoord[0]
		self.c = listeCoord[1]
		self.produits = {}
		for produitID in listeProduit:
			if produitID in self.produits.keys():
				self.produits[produitID] += 1
			else:
				self.produits[produitID] = 1
			
	
