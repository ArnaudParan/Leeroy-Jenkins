# -*- coding: utf-8 -*-

def write_commands(output, output_path, file_number=1):
    save_folder = os.path.dirname(output_path)
    save_file = os.path.basename(output_path)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    #print "Writting results in file : " + output_path + " ..." 

    # SAVE HERE
    with open(save_folder+'/'+str(file_number)+save_file,'wb') as sf:
        #sf.write( [ ';'.join(l)+'\n' for l in data ] )
        sf.write(str(len(output))+'\n')

        for line in output:
            sf.write(line+'\n')


 def commands():
    coms = []
    # drawing commands
    for d in to_draw:
        

    return coms
  
def assign_warehouse(client):
    d = Array()
    d[0] = dist(client, 0)
    d_min = d[0]
    arg_min = 0
    for w in range(1,W):
        d[w] = dist(client, w)
        if(d[w] < d_min):
            d_min == d[w]
            arg_min = w
    return w
    
def assign_warehouse_cycle():
    for c in client:
        assign_warehouse(c)
        
class Client:
    def __init__(self,r,c,demands_list):
        self.r = r
        self.c = c
        # demands est la liste de besoins du client
        self.demands = to_dict(demands_list)
        self.wh = assign_warehouse(self)
    def actualize_demand(self, product_transfer):
        # product_transfer est un dictionnaire dont les clés sont les
        # clés des produits, et les qté associées sont les qté algébriquement ajoutées
        self.demands = add_dict(self.demands,product_transfer)
    
def to_dict(list):
    dict output
    for key in range(0,len(list)):
        output[key] = list[key]
    return output

# dict1 est toujours le dictionnaire de plus grande taille
def add_dict(dict1, dict2):
    for key in dict1:
        if(dict2[key] == None):
            dict2[key] = dict1[key]
        else:
            dict2[key] += dict1[key]
    return dict2