## Kata 6 ejercicio 2
planetas = [ 'Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Nepturno' ]

ing_plan = input("Ingrese el nombre de un plenta comenzando con mayuscula: ")
print("", ing_plan)
plan_index = planetas.index(ing_plan)
print(" ",planetas)
print("El planeta mas cerca es: /n " + ing_plan)

##print(planetas [ 0 : ing_plan ])

print("El planetas mas cercano es: /n" + ing_plan)

print(planetas[plan_index + 1:])