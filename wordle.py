palabra = 'cielo'
letras_verificadas = []
intentos = 6        
palabra_correcta = list(palabra)


print('Bienvenido a Wordle Python Edition')
print('Tiene 6 intentos\nAdivine la palabra')
print(f'La palabra a adivinar contiene {len(palabra_correcta)} letras\n')
letra = input('Por favor ingrese la palabra\n')

def verificador_palabra(palabra_correcta,intentos):
    for turnos in range(intentos):
        palabras = list(letra)
        letras_iguales = palabras[turnos] == palabra_correcta[turnos]
        letra_existe = palabras[turnos] in palabra_correcta
        if letras_iguales:
            print(f'Le quedan [{intentos}] intentos')
            print('Ingrese otra palabra\n')
            letras_verificadas.append(f"[{palabras[turnos]}]")
            print(letras_verificadas)
        elif letra_existe:
            print(f'Le quedan [{intentos}] intentos')
            print('Ingrese otra palabra\n')
            letras_verificadas.append(f"({palabras[turnos]})")
            print(letras_verificadas)
        elif palabras == palabra_correcta:
             print('Felicidades, ganaste el juego')
        else:
            letras_verificadas.append(palabras[turnos])
    
    intentos = intentos - 1
    return letras_verificadas

verificador_palabra(palabra_correcta,intentos)

print(f'La palabra correcta era {palabra}')
print('Gracias por jugar, vuelta pronto')