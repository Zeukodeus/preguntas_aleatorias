print ("responda las preguntas siguiendo estas normas: ")
print ("1. Para preguntas de nombres solo el primer nombre y el primer apellido")
print ("2. Para nombres propios siempre en mayúscula")
print ("3. sin finalizar en punto")
print ("4. Con tildes")

import random

# Define una lista de preguntas y respuestas
preguntas_respuestas = [
    ('¿Cuál es la capital de España?', 'Madrid'),
    ('¿En qué año se descubrió América?', '1492'),
    ('¿Quién escribió "El Quijote"?', 'Miguel de Cervantes'),
    ('¿Quién pintó la Mona Lisa?', 'Leonardo da Vinci'),
    ('¿Cuál es el río más largo del mundo?', 'Amazonas'),
    ("¿En qué año se aprobó la actual Constitución española?", "1978"),
    ('¿En qué año murió Freddie Mercury?', '1991'),
    ('¿Quién inventó la bombilla?', 'Thomas Edison'),
    ('¿En qué país se usó la primera bomba atómica?', 'Japón'),
    ('¿Cuándo empezó la Primera Guerra Mundial?', '1914'),
    ('¿En qué año se produjo la Revolución Francesa?', '1789'),
    ('¿Cuántas veces ha estado el hombre en la Luna?', '6'),
    ('¿Qué presidente de Estados Unidos fue asesinado en Dallas?', 'John Kennedy'),
    ('¿Cuándo se extinguieron los dinosaurios (en años)?', '66000000'),
    ('¿Según la Biblia, ¿cuántos años vivió Matusalén?', '969'),
    ('¿Cuál es el libro más vendido de la historia?', 'La Biblia'),
]

while True:
    # Genera una pregunta aleatoria y muestra la pregunta
    pregunta, respuesta = random.choice(preguntas_respuestas)
    print(pregunta)

    # Pide al usuario que ingrese una respuesta
    respuesta_usuario = input('Respuesta: ')

    # Comprueba si la respuesta es correcta y muestra la respuesta correcta
    if respuesta_usuario == respuesta:
        print('¡Respuesta correcta!')
    else:
        print('Respuesta incorrecta. La respuesta correcta es:', respuesta)

    # Pregunta si el usuario desea continuar
    continuar = input('¿Desea continuar? (S/N): ')
    if continuar.lower() != 's':
        break