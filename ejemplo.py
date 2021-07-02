Lado1 = float(input("Ingresa el primer lado "))
Lado2 = float(input("Ingresa el segundo lado "))

área = Lado1*Lado2
print ("El área es:", área)

if área<30 :
    print ("Su observación es: área pequeña")
elif 30<= área <60:
    print ("Su observación es: área mediana")
elif 60<= área <90:
    print ("Su observación es: área grande")
else :
    print ("Su observación es: área tamaño Jumbo")
   

