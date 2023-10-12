# Obtener una lista de oraciones.
# Contar cuántas palabras hay en cada oración.
# Para cada oración en qué posiciones aparece por primera vez la palabra "Python".
# ¿Cuántas veces aparece la palabra "Python" en cada oración?
# Cuál es el promedio (por oración) de apariciones la palabra "Python"?
# ¿Cuántas veces aparece la palabra "Python" el texto competo. Guardar este resultado en la variable python_count.
# De qué tipo es esta variable?

text = "Python is a great language. It is relatively easy to learn and has an intuitive syntax. The rich selection of libraries also contribute to the popularity and success of Python. However, it is not just about the third party libraries. Base Python also provides numerous methods and functions to expedite and ease the typical tasks in data science."

sentence = ""
list = []


for letter in text:
    if letter != ".":
        sentence += letter
    else:
        sentence += letter
        list.append(sentence) 
        # print(list)
        sentence = ""

print(list)