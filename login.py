
users = {
    "bryan": '0880',
    "yoel": '1234',
    "ryan": '4321',
}


saldos = {
    "bryan": 0.0,
    "yoel": 0.0,
    "ryan": 0.0
}

def mostrar():
    print('1. Agregar Balance a la Cuenta')
    print('2. Retirar Balance')
    print('3. Ver Balance')
    print('4. Depositar')
    print('5. Cambiar de Cuenta')
    print('6. Salir\n')

def agregar(usuario):
    saldos[usuario]
    agreg = float(input("Ingrese un balance para agregar a la cuenta: \n"))
    saldos[usuario] += agreg
    print(f'El saldo actual es {saldos[usuario]}\n')

def retirar(usuario):
    saldos[usuario]
    retirar = float(input('Diga el balance a retirar: \n'))
    if retirar <= saldos[usuario]:
        saldos[usuario] -= retirar
        print(f'El saldo actual es {saldos[usuario]}\n')
    else:
        print('Fondos insuficientes')

def ver_balance(usuario):
    print(f'El saldo actual es {saldos[usuario]}\n')

def depositar(usuario):
    saldos[usuario] 
    while True:
        user_a_Transferir = input('Diga a quien le va a transferir:\n').strip().lower()
        if user_a_Transferir  in users:
            cantidad = float(input("digame la cantidad a transferir:\n"))
            if cantidad > saldos[usuario]:
                print("saldos insuficientes\n")
            else:
                saldos[user_a_Transferir] += cantidad
                saldos[usuario] -= cantidad
                print(f'Transferencia exitosa, {cantidad} a {user_a_Transferir}')
                print(f'te quedan {saldos[usuario]} pesos')
                break
        else:
            print("Usuario no identificado")
    
    
    
def salir(usuario):
    while True:
        salir_clave = input(f'{usuario}, escriba su clave de usuario para salir: \n')
        if salir_clave == users[usuario]:
            print("salida exitosa\n")
            exit()
        else:
            print("Clave incorrecta\n")
    

def menu():
    intentos = 2
    
    while True:
        global usuario
        usuario = input('Escribe tu nombre de usuario: \n').strip()
        contra = input('Escribe tu contraseña: \n').strip()
        if intentos == 0:
            print('se acabaron los intentos... regresa pronto\n')
            exit()
            
        if usuario in users and users[usuario] == contra:
            print("Accediste correctamente\n")
            while True:
                mostrar()
                option = input('Seleccione una opción:\n')
                if option == '1':
                    agregar(usuario)
                elif option == '2':
                    retirar(usuario)
                elif option == '3':
                    ver_balance(usuario)
                elif option == '4':
                    depositar(usuario)
                elif option == '5':
                    menu()
                elif option == '6':
                    salir(usuario)
                else:
                    print('Opcion no valida\n')
        else:
            print('Credenciales incorrectas\n')
            intentos -= 1

menu()


