import sys
import math

# Entrée d'initialisation -----------------------------------------------------------------------------
factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories pour i=factory_count-1 alors link_count= i(1+1)/2

# list des distances entre n factories 
# [(0,1,d), (0,2,d), ... (0,n,d), (1,2,d), ... (1,n,d), (2,3,d), ..., (n-1,n,d)]
factory_list = [0] * link_count
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    factory_list[i] = factory_1, factory_2, distance 
# to print factory_list : print(factory_list)

# game loop -------------------------------------------------------------------------------------------
while True:
    entity_count = int(input())     # the number of entities (e.g. factories and troops)
    entity_list = []
    id_list_fact = []               # list des usines par id
    id_list_fact_neutr = []         # list des usines neutres par id
    id_list_fact_bot = []           # list des usines enemies par id
    id_list_fact_owned = []         # list des usines amies par id
    id_list_troop = []              # list des troop par id

    for i in range(entity_count):
        inputs = input().split()
        entity_id = int(inputs[0])  # entity name 0, 1, 2, etc. 
        entity_type = inputs[1]     # "FACTORY" or "TROOP"
        arg_1 = int(inputs[2])      # entity owner 1=me -1=bot 0=neutral
        arg_2 = int(inputs[3])      # FACTORY nb cyborg dans l'usine    #TROOP id usine de départ
        arg_3 = int(inputs[4])      # FACTORY production 0-3            #TROOP id usine d'arrivée
        arg_4 = int(inputs[5])      # FACTORY --                        #TROOP nb cybarg dans la troupe
        arg_5 = int(inputs[6])      # FACTORY --                        #TROOP distance de la cible
        
        entity_list.append(inputs)

        if entity_type == "FACTORY" :                       # list des usines / troop par id
            id_list_fact.append(entity_id)
        else : 
            id_list_troop.append(entity_id)

        if entity_type == "FACTORY" and arg_1 == 0 :        # list des usines neutres par id
            id_list_fact_neutr.append(entity_id)

        if entity_type == "FACTORY" and arg_1 == -1 :       # list des usines enemies par id
            id_list_fact_bot.append(entity_id)
            
        id_list_fact_not_owned = id_list_fact_neutr + id_list_fact_bot
        id_list_fact_not_owned.sort()                       # list des usines enemies OU neutre

        if entity_type == "FACTORY" and arg_1 == 1: 
            id_list_fact_owned.append(entity_id)            # list des usines amies par id

    # Fonctions de tri ----------------------------------------------------------------------------------------
    # list d'id choisi puis trié par ordre croissant suivant un critère
    def organise(list_1, index, reverse) :
        list_to_organise = list_1
        list_to_organise.sort(key=lambda x : x[index], reverse=reverse)
        return(list_to_organise)

    # filtre supprime les entity non amie dans une list
    def filtre_not_owned(list_1):
        list_filtre = []
        for id in id_list_fact_not_owned :
            list_filtre.append(entity_list[id])
        return(list_filtre)

    # quelle est mon usines la plus peuplée ?
    def my_biggest_army(id_list) :
        list_to_compare = [] 
        for id in id_list :
            list_to_compare.append(entity_list[id])
        return(max(list_to_compare, key=lambda x : x[3]))

    # quelle est la plus petite armée d'une liste d'ID ?
    def smallest_army_target(id_list) :
        list_to_compare = []
        for id in id_list :
            list_to_compare.append(entity_list[id])
        return(min(list_to_compare, key=lambda x : x[3]))

    # quelle est la distance entre deux usines id1 et id2 ?
    def distance(a, b) : 
        dist = 0
        x, y = min(a, b), b
        for i in range(len(factory_list)) : 
            if (factory_list[i][0] == x) and (factory_list[i][1] == y) :
                dist = factory_list[i][2]
        return(dist)


    # Choix de la cible ---------------------------------------------------------------------------------------------
    # priority chart

    priority_list = [] # list id des cibles potentiel et score associé [[id, score], [id, score], [id, score]]
    for id in id_list_fact_not_owned :
        lst = [int(id), 0]
        priority_list.append(lst)

    # neutre ou enemi
    for target in priority_list : 
        if target[0] in id_list_fact_neutr : # +100 pts si la cible est neutre
            target[1] += 100
    
    # production (critère index 4)
    prod_list_not_owned = filtre_not_owned(entity_list)
    score_prod_list = []     #creation d'une liste de score 
    for e in prod_list_not_owned : 
        score_prod_list.append( [ int(e[0]) , int( e[4] )*10 ] )
    score_prod_list.sort(key=lambda x : x[0])

    for i in range(len(priority_list)) : # addition des scores
        priority_list[i][1] += score_prod_list[i][1]
 
    # taille de l'armée (critère index 3)
    garnison_list_not_owned = filtre_not_owned(entity_list)

    score_garnison_list = []     #creation d'une liste de score 
    for e in garnison_list_not_owned : 
        score_garnison_list.append( [ int(e[0]) , int( e[3] )*-2 ] )
    score_garnison_list.sort(key=lambda x : x[0])

    for i in range(len(priority_list)) : # addition des scores
        priority_list[i][1] += score_garnison_list[i][1]




    priority_list.sort(key=lambda x : x[1], reverse=True)
    # Test : print(priority_list)
    target = priority_list[0][0]


    # declaration pour le tour --------------------------------------------------------------------------------------
    # MOVE
    source = int(my_biggest_army(id_list_fact_owned)[0])
    destination = int(target)
    dist = int(distance(source, destination))
    opponent = int(entity_list[target][3])
    cyborgCount = 1 + opponent + dist

    ordre = "MOVE "+str(source)+" "+str(destination)+" "+str(cyborgCount)

    # WAIT
    my_army = int(my_biggest_army(id_list_fact_owned)[3])
    if my_army < cyborgCount :
        ordre = "WAIT"

    # Envoi 
    print(ordre)


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

