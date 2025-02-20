else:
    match option:
                            case 1:
                                Equipos = []
                                isEquipo = True
                                while isEquipo:
                                    os.system('cls')
                                    nombre =[input('ingrese el nombre del equipo: ')]
                                    equipo =[nombre]
                                    Equipos.append(equipo)
                                    isEquipo = input('desea agregar otro equipo S/N : ').upper()== 'S'
                                if isEquipo == 'S':
                                        continue
                                print(Equipos)
                                LIGA_BETPLAY.append(Equipos)