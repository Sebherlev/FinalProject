x=1
total=0
while x<=10:
    nota=int(input("Ingrese la nota: "))
    if nota>=11:
        total=total+1
    x=x+1
print("Han aprobado ",total)
