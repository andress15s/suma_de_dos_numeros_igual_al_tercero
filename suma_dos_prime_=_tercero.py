print("-----------------------------------------------------")
print("-----suma_de_dos_numeros_es_igual_al_tercero---------")
print("-----------------------------------------------------")


#input

x = int(input("ingrese el primer numero: "))
y = int(input("ingrese el segundo numero: "))
z = int(input("escriba el tercer numero: "))

# processing

if x + y == z:
    print(str(x) + "  +  " + str(y) + " es igual a " + str(z))

else: 
    print("la suma de los dos primeros no son iguales al tercero")