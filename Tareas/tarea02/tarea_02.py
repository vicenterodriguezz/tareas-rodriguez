
"""TAREA_02_RODRIGUEZ


El archivo original se encuentra en:
    https://colab.research.google.com/drive/1taCDODah7yhcki0cT4PmxrWADcPaPN-T
"""



"""# TAREA 02 VICENTE RODRÍGUEZ

**Problema 1**
"""

print("Los números del -100 al 200 son:") #esto sería el encabezado antes del listado
for x in range (-100, 201): #aquí se define el rango a usar
  print(x) #la x representa el rango, por lo tanto, basta imprimir eso para mostrar el listado completo

"""**Problema 2**"""

print("Los números del -100 al 200 divisibles entre 6 son:") #encabezado antes del listado
for x in range(-100, 201): #se define el rango
  if x % 6 == 0: #esto permitirá acotar el rango, solo a los divisible por 6
    print(x)

"""**Problema 3**"""

print("Pseudocódigo, Sumador y comparador de dos números:") #encabezado
def sumador(num1, num2):#se identifica el orden de los números que se definirán para sumar
  suma = num1 + num2 #se define el tipo de operación matemática que se desea hacer con los números que entren
  if suma < 200:
    mensaje = "menor a 200" #se define que, si la suma es menor a 200, se mostrará el mensaje final que está entre comillas
  elif suma < 250:
    mensaje = "mayor a 200 y menor a 250" #se define que, si la suma es mayor a 200 y menor a 250, se mostrará el mensaje final que está entre comillas
  else:
    mensaje = "mayor a 250" #se define que, si la suma es mayor a 250, se mostrará el mensaje final que está entre comillas

#el uso de los comandos if, elif y else, es clave para ordenar y tener un mensaje para los tres tipos de respuestas posibles

  print(f"La suma de {num1} y {num2} es {suma}, entonces es {mensaje}.") #este es el mensaje que aparecerá antes del mensaje final

#ejemplos del código:
sumador(98, 33)
sumador(180, 22)
sumador(200, 150)
#aquí se ingresan los números que se desean sumar, siguiendo la estructura del orden definido en un inicio

"""**Problema 4**"""

def evaluar_mayor_de_edad_y_gusto_musical(edad, gusta_musica_urbana): #se definen los dos factores a evaluar: la edad y el gusto musical (sí o no)
  if edad > 18: #como se pide identificar la mayoría de edad, se usa un 18 que representa: si tiene más de 18 años...
    if gusta_musica_urbana: #este es para el segundo factor, el gusto musical
      print("Eres mayor de edad y te gusta la música urbana") #al cumplirse ambos, el mensaje entre comillas es el que aparecerá cuando se ingresen los datos. Se aplica la misma lógica en el resto de respuestas, según cada dato
    else:
      print("Eres mayor de edad y no te gusta la música urbana")
  else:
    if gusta_musica_urbana:
      print("Eres menor de edad y te gusta la música urbana")
    else:
      print("Eres menor de edad y no te gusta la música urbana")

#ejemplos del código:
evaluar_mayor_de_edad_y_gusto_musical(30, True)
evaluar_mayor_de_edad_y_gusto_musical(15, True)
evaluar_mayor_de_edad_y_gusto_musical(19, False)
evaluar_mayor_de_edad_y_gusto_musical(14, False)

#para ejemplificar el resultado de la función, se usaron las cuatro respuestas posibles respecto a la edad y el gusto musical