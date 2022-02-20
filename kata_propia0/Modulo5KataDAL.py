planeta_seg = input("Ingresa distancia del sol para planeta 2 en KM: ")
platena_prim = input("Ingresa distancia del sol para planeta 1 en KM: ")
planeta_seg = int(planeta_seg)
platena_prim = int(platena_prim)
distkm = planeta_seg - platena_prim
print(distkm)
#comvesion km a Milla
distmilla = distkm * 0.621
print(abs(distmilla))