#Victor
#CLASSE ZONE

import warehouse.py

def square_distance2(r1, c1, r2, c2):
    return ((r1 - r2)**2) + ((c1 - c2)**2)

class zone:
	def __init__(self, warehouse0, listeClients0, listeDrones0):
		self.warehouse = warehouse0
		self.clients = listeClients0
		self.drones = listeDrones0
		self.demandeGlobale={}
		self.demandeZone()
		
	def demandeZone(self):
		for client in self.clients:
			for produitID in client.demands.keys():
				if produitID in self.demandeGlobale.keys():
					self.demandeGlobale[produitID] += client.demands[produitID]
				else:
					self.demandeGlobale[produitID] = client.demands[produitID]

def nearest_warehouse(initR, initC, listeWarehouse):
	nearestWarehouseId = 0
	currDistance = square_distance2(initR, initC, listeWarehouse[0].r, listeWarehouse[0].c)
	for id,warehouse in enumerate(listeWarehouse):
		if currDistance > square_distance2(warehouse.r, warehouse.c, initR, initC):
			currDistance = square_distance2(warehouse.r, warehouse.c, initR, initC)
			nearestWarehouseID = id
	return nearestWarehouseId
					
def repartitionZone(listeWarehouse, listeClient, listeDrone):
	#Attention encore à modifiier
	n = len(listeWarehouse)
	listeRepartitionWarehouse = []
	for client in listeClient:
		listeRepartitionWarehouse.append(nearest_warehouse(client.r, client.c, listeWarehouse))
	
	for idWarehouse in range(n):
		listeClientSurWarehouse=[]
		for idClient, warehousAffecte in enumerate(listeRepartitionWarehouse):
			if warehousAffecte == idWarehouse:
				listeClientSurWarehouse.append(idClient)
			listeZone.append(zone(listeWarehouse[idWarehouse],listeClientSurWarehouse, listeDrone))
	
	# for idWarehouse,warehouse in enumerate(listeWarehouse):
		# listeClientSurWarehouse = []
		# for idClient, warehousAffecte in enumerate(listeRepartitionWarehouse):
			# if warehousAffecte == idWarehouse:
				# listeClientSurWarehouse.append(idClient)
		# listeZone.append(zone(warehouse,listeClientSurWarehouse, listeDrone)
		
	return listeZone
	
	

if __name__=="__main__":


