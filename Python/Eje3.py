# Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales. 
print("Ingrese su peso en KG")
peso = input()
print("Ingrese su altura en metros")
altura = input()
imc = peso/pow(altura,2)
print(round(imc,2))
