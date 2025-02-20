#Declara una lista
frutas = []
vocales = ['a','e','i','o']
#tamaño de una lista
print(len(vocales))
#acceder elemento
print(vocales[1])
print(vocales[-1])
#agregar elementos lista
#frutas.append(input('ingrese una fruta :'))
#frutas.append('uvas')
#print(frutas)
#for vocal in vocales:
#    print(vocal)

for idx,vocal in enumerate(vocales):
    print(f'idx {idx} vocal {vocal}')

if 'uvas' in frutas:
    print('ya compro uvas')
    