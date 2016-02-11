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
        
        