import os
def saludar(nombre:str):
    print(f'hola mundo {nombre}')

def sumar(num1:int, num2:int):
    return num1 + num2

if __name__ == '__main__':
    num1 =int(input('ingrese un numero: '))
    num2 = int(input('ingrese el numero 2: '))
    print(sumar(num1,num2))
    os.system('pause')
    
