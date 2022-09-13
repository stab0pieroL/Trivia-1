print ("Bienvenido a mi trivia sobre fútbol")
print ("Pondremos a prueba tus conocimientos")

nombre = input("Ingresa tu nombre: ")
puntaje = 0

print ("\n Hola",nombre,",responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n")

# Pregunta 1
print ("1) ¿Cuál es el país creador del fútbol moderno?\n a) Francia\n b) Suecia\n c) China\n d) Inglaterra")

respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a","b","c","d"):
  respuesta_1 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_1 == "d":
  puntaje += 1
  print("Muy bien",nombre, "!")
else:
  print("Incorrecto")     
     
# Pregunta 2
print ("\n2) ¿En qué año se realizo la Primera Copa Mundial de Fútbol organizado por la FIFA?\n a) 1924\n b) 1934\n c) 1930\n d) 1920")

respuesta_2 = input("\nTu respuesta: ")

while respuesta_2 not in ("a","b","c","d"):
  respuesta_2 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_2 == "c":
  puntaje += 1
  print("Muy bien",nombre, "!")
else:
  print("Incorrecto")  


# Pregunta 3
print ("\n3) ¿Qué país gano la primera Copa Mundial de Fútbol?\n a) Uruguay\n b) Brasil\n c) Alemania\n d) Francia")

respuesta_3 = input("\nTu respuesta: ")

while respuesta_3 not in ("a","b","c","d"):
  respuesta_3 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_3 == "a":
  puntaje += 1
  print("Muy bien",nombre, "!")
else:
  print("Incorrecto")
    

# Pregunta 4
print ("\n4) ¿Qué país es el más ganador de la Copa mundial de Fútbol?\n a) Alemania\n b) Italia\n c) Brasil\n d) España")

respuesta_4 = input("\nTu respuesta: ")

while respuesta_4 not in ("a","b","c","d"):
  respuesta_4 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_4 == "c":
  puntaje += 1
  print("Muy bien",nombre, "!")
else:
  print("Incorrecto")  
    

# Pregunta 5
print("\n5) ¿Cuál es el jugador de fútbol con mayor Balones de Oro?\n a) Neymar\n b) Cristiano Ronaldo\n c) Ronaldinho\n d) Lionel Messi")

respuesta_5 = input("\nTu respuesta: ")

while respuesta_5 not in ("a","b","c","d"):
  respuesta_5 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_5 == "d":
  puntaje += 1
  print("Muy bien",nombre, "!")
else:
  print("Incorrecto")

    
# Pregunta 6
print("\n6) ¿A cuántas Copas del Mundo asistió la Selección Peruana de Fútbol?\n a) 7\n b) 6\n c) 5\n d) 4")

respuesta_6 = input("\nTu respuesta: ")

while respuesta_6 not in ("a","b","c","d"):
  respuesta_6 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_6 == "c":
  puntaje += 1
  print("Muy bien",nombre, "!")
else:
  print("Incorrecto")


# Pregunta 7
print("\n7) ¿Cuál fue el último club campeón de la UEFA Champions League?\n a) Paris Saint-German\n b) Bayern Munich\n c) Real Madrid\n d) Manchester City")

respuesta_7 = input("\nTu respuesta: ")

while respuesta_7 not in ("a","b","c","d"):
  respuesta_7 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_7 == "c":
  puntaje += 1
  print("Muy bien",nombre, "!")
else:
  print("Incorrecto") 


# Pregunta 8
print("\n8) ¿Cuál fue el único equipo peruano en ganar una competición internacional oficial de Conmebol?\n a) Universitario de deportes\n b) Alianza Lima\n c) FBC Melgar\n d) Cienciano")

respuesta_8 = input("\nTu respuesta: ")

while respuesta_8 not in ("a","b","c","d"):
  respuesta_8 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_8 == "d":
  puntaje += 1
  print("Muy bien",nombre, "!")
else:
  print("Incorrecto")


# Pregunta 9
print("\n9) ¿Cuál es el equipo peruano más ganador de la Primera división del torneo local según la Federación Peruana de Fútbol?\n a) Sport Boys\n b) Alianza Lima\n c) Universitario de Deportes\n d) Sporting Cristal")

respuesta_9 = input("\nTu respuesta: ")

while respuesta_9 not in ("a","b","c","d"):
  respuesta_9 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_9 == "c":
  puntaje += 1
  print("Muy bien",nombre, "!")
else:
  print("Incorrecto") 


# Pregunta 10
print("\n10) ¿Cuál fue el equipo de la primera división del fútbol peruano que desdendió de categoría y ascendio el siguiente año por medios legales?\n a) Alianza Lima\n b) Cusco FC\n c )San Martín\n d) Piratas FC")

respuesta_10 = input("\nTu respuesta: ")

while respuesta_10 not in ("a","b","c","d"):
  respuesta_10 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_10 == "a":
  puntaje += 1
  print("Muy bien!",nombre, "!")
else:
  print("Incorrecto") 


print("Tu puntaje es: ",puntaje)

print("Gracias por jugar la trivia del fútbol!")