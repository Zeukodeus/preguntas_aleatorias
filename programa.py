import random

# Define una lista de preguntas y respuestas
preguntas_respuestas = [
    ('¿Cuál es la capital de España?', 'Madrid'),
    ('¿En qué año se descubrió América?', '1492'),
    ('¿Quién escribió "El Quijote"?', 'Miguel de Cervantes'),
    ('¿Quién pintó la Mona Lisa?', 'Leonardo da Vinci'),
    ('¿Cuál es el río más largo del mundo?', 'Amazonas'),
    ('¿En qué país se encuentra la Torre Eiffel?', 'Francia'),
]

# Repite hasta que el usuario desee detenerse
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