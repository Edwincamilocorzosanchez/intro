import limpiar as sc
def ValidateInt(msg:str)->int:
    try:
        x = int(input(msg))
    except ValueError:
        print('El valor ingresado no es válido')
        sc.pausar_pantalla()
        return ValidateInt(msg)
    else:
        return x
    
def ValidateFloat()->float:
    try:
        x = float(input(')..'))
    except ValueError:
        print('El valor ingresado no es válido')
        sc.pausar_pantalla()
        return ValidateFloat()
    else:
        return x