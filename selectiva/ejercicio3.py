#un grupo de 10 estudiantes presentan un examen de algoritmia. 
# Hacer un algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e imprima:

estudiante1=int(input("calificacion 1: "))
estudiante2=int(input("calificacion 2: "))
estudiante3=int(input("calificacion 3: "))
estudiante4=int(input("calificacion 4: "))
estudiante5=int(input("calificacion 5: "))
estudiante6=int(input("calificacion 6: "))
estudiante7=int(input("calificacion 7: "))
estudiante8=int(input("calificacion 8: "))
estudiante9=int(input("calificacion 9: "))
estudiante10=int(input("calificacion 10: "))


puntajeMenor50=0
puntajeMayor50Menor70=0
puntajeMenor70Mayor80=0
puntajeMayor80=0


if estudiante1>=1 and estudiante1<=49:
    puntajeMenor50 +=1 
elif estudiante1>=50 and estudiante1<=69:
    puntajeMayor50Menor70 +=1  
elif estudiante1 >=70 and estudiante1<=79:
    puntajeMenor70Mayor80 +=1  
elif estudiante1 >=80 and estudiante1<=100:
    puntajeMayor80 +=1

if estudiante2>=1 and estudiante2<=49:
    puntajeMenor50 +=1 
elif estudiante2>=50 and estudiante2<=69:
    puntajeMayor50Menor70 +=1  
elif estudiante2 >=70 and estudiante2<=79:
    puntajeMenor70Mayor80 +=1  
elif estudiante2 >=80 and estudiante2<=100:
    puntajeMayor80 +=1

if estudiante3>=1 and estudiante3<=49:
    puntajeMenor50 +=1 
elif estudiante3>=50 and estudiante3<=69:
    puntajeMayor50Menor70 +=1  
elif estudiante3 >=70 and estudiante3<=79:
    puntajeMenor70Mayor80 +=1  
elif estudiante3 >=80 and estudiante3<=100:
    puntajeMayor80 +=1

if estudiante1>=4 and estudiante4<=49:
    puntajeMenor50 +=1 
elif estudiante4>=50 and estudiante4<=69:
    puntajeMayor50Menor70 +=1  
elif estudiante4 >=70 and estudiante4<=79:
    puntajeMenor70Mayor80 +=1  
elif estudiante4 >=80 and estudiante4<=100:
    puntajeMayor80 +=1

if estudiante5>=1 and estudiante5<=49:
    puntajeMenor50 +=1 
elif estudiante5>=50 and estudiante5<=69:
    puntajeMayor50Menor70 +=1  
elif estudiante5 >=70 and estudiante5<=79:
    puntajeMenor70Mayor80 +=1  
elif estudiante5 >=80 and estudiante5<=100:
    puntajeMayor80 +=1

if estudiante6>=1 and estudiante6<=49:
    puntajeMenor50 +=1 
elif estudiante6>=50 and estudiante6<=69:
    puntajeMayor50Menor70 +=1  
elif estudiante6 >=70 and estudiante6<=79:
    puntajeMenor70Mayor80 +=1  
elif estudiante6 >=80 and estudiante6<=100:
    puntajeMayor80 +=1

if estudiante7>=1 and estudiante7<=49:
    puntajeMenor50 +=1 
elif estudiante7>=50 and estudiante7<=69:
    puntajeMayor50Menor70 +=1  
elif estudiante7 >=70 and estudiante7<=79:
    puntajeMenor70Mayor80 +=1  
elif estudiante7 >=80 and estudiante7<=100:
    puntajeMayor80 +=1

if estudiante8>=1 and estudiante8<=49:
    puntajeMenor50 +=1 
elif estudiante8>=50 and estudiante8<=69:
    puntajeMayor50Menor70 +=1  
elif estudiante8 >=70 and estudiante8<=79:
    puntajeMenor70Mayor80 +=1  
elif estudiante8 >=80 and estudiante8<=100:
    puntajeMayor80 +=1

if estudiante9>=1 and estudiante9<=49:
    puntajeMenor50 +=1 
elif estudiante9>=50 and estudiante9<=69:
    puntajeMayor50Menor70 +=1  
elif estudiante9 >=70 and estudiante9<=79:
    puntajeMenor70Mayor80 +=1  
elif estudiante9 >=80 and estudiante9<=100:
    puntajeMayor80 +=1

if estudiante10>=1 and estudiante10<=49:
    puntajeMenor50 +=1 
elif estudiante10>=50 and estudiante10<=69:
    puntajeMayor50Menor70 +=1  
elif estudiante10 >=70 and estudiante10<=79:
    puntajeMenor70Mayor80 +=1  
elif estudiante10 >=80 and estudiante10<=100:
    puntajeMayor80 +=1


print ("La cantida de estudiantes que obtuvieron una calificacion menor a 50: ",puntajeMenor50)
print ("La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70: ",puntajeMayor50Menor70)
print ("La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80: ",puntajeMenor70Mayor80)
print ("La cantidad de estudiantes que obtuvieron una calificación de 80 o más son: ", puntajeMayor80)


