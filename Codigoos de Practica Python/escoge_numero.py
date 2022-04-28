import random

def run():
    numero_azar = random.randint(1,100)
    numero= int(input('!Adivina¡ Ingresa un numero: '))
    INTENTOS=5
    if numero == numero_azar:
        PrinT('!Ganaste¡ Adivinaste el numero '+numero_azar+ 'al primer intento')
    else:
        while numero_azar != numero :
            INTENTOS-=1
            print('   !te quedan '+str(INTENTOS)+' intentos¡')    
            if INTENTOS != 0:
                if numero < numero_azar:
                    print('--Debe ser un numero mayor--')
                elif numero > numero_azar:
                    print('--Debe ser un nummero menor--')     
            elif INTENTOS == 0:
                print('!Fin del Juego¡ superaste los intentos')
                print('EL numero ganador era: '+str(numero_azar))
                break   
            numero= int(input('Ingresa de nuevo un numero: '))
            if numero == numero_azar:
                print('!Ganaste¡ adivino el:'+str(numero_azar))
                break        

if __name__=='__main__':
    run()