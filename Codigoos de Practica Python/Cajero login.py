  
def tipo_cuenta(opcion): #utilice un función con parametro y dentro una condición encadenada
    if opcion == 1:
        print('Cuenta de Ahorros')
    elif opcion == 2:
        print('Ceunta Corriente')
    else:
        print('¡Ingresa una cuenta valida!')       

def pas():
    print('Bienvenido')
    clave = input('Crear clave: ') 
    confirma_clave = input('Confirma la clave: ') 
    if clave == confirma_clave: 
        menu='''Transferir a cuenta:
        1- Ahorros
        2- Corriente
        Elige una opción (1,2): ''' 
        escribe = int(input(menu))
        tipo_cuenta(escribe)
        return clave 
    else:
        while  clave != confirma_clave:
            print('¡ Intentelo nuevamente las claves no coinciden !')
            pas()
            break     
def run():    
    
    
    resul=pas()
    print('Clave generada: '+ resul)

if __name__=='__main__':
    run()