import random
import Ascii_Art

#Bugs
# Check Organo multicolor puede ser ayudado por cualquier medicina          (OK)
# Se pueden lanzar medicinas al tablero sin que hayan organos
# Check en inputs que las entradas sean numericas en un rango
# Desarrollar intro                                                         (OK)


numero_jugadores = 0
turno_jugador = 0

mano_pl1  =[]
mano_pl2  =[]
mano_pl3  =[]
mano_pl4  =[]
mano_pl5  =[]
mano_pl6  =[]

mesa_pl1  =[]
mesa_pl2  =[]
mesa_pl3  =[]
mesa_pl4  =[]
mesa_pl5  =[]
mesa_pl6  =[]

mazo_descartes = []
num_descartes  = 0
#reintento = 0

ganador = 0
ganador_texto = 0


Organo_Rojo         = ["Organo Rojo", "Organo Rojo", "Organo Rojo", "Organo Rojo", "Organo Rojo"]
Organo_Azul         = ["Organo Azul", "Organo Azul", "Organo Azul", "Organo Azul", "Organo Azul"]
Organo_Amarillo     = ["Organo Amarillo", "Organo Amarillo", "Organo Amarillo", "Organo Amarillo", "Organo Amarillo"]
Organo_Verde        = ["Organo Verde", "Organo Verde", "Organo Verde", "Organo Verde", "Organo Verde"]
Organo_Multicolor   = ["Organo Multicolor"]
Virus_Rojo          = ["Virus Rojo", "Virus Rojo", "Virus Rojo", "Virus Rojo", "Virus Rojo"]
Virus_Azul          = ["Virus Azul", "Virus Azul", "Virus Azul", "Virus Azul", "Virus Azul"]
Virus_Amarillo      = ["Virus Amarillo", "Virus Amarillo", "Virus Amarillo", "Virus Amarillo", "Virus Amarillo"]
Virus_Verde         = ["Virus Verde", "Virus Verde", "Virus Verde", "Virus Verde", "Virus Verde"]
Virus_Multicolor    = ["Virus Multicolor"]
Medicina_Roja       = ["Medicina Roja","Medicina Roja","Medicina Roja","Medicina Roja"]
Medicina_Azul       = ["Medicina Azul","Medicina Azul","Medicina Azul","Medicina Azul"]
Medicina_Amarilla   = ["Medicina Amarilla","Medicina Amarilla","Medicina Amarilla","Medicina Amarilla"]
Medicina_Verde      = ["Medicina Verde","Medicina Verde","Medicina Verde","Medicina Verde"]
Medicina_Multicolor = ["Medicina Multicolor","Medicina Multicolor","Medicina Multicolor","Medicina Multicolor"]
Transplante         = ["Transplante", "Transplante", "Transplante"]
Error_Medico        = ["Error Medico"]
Guante_Latex        = ["Guante Latex"]
Contagio            = ["Contagio", "Contagio"]
Ladron_Organos      = ["Ladron Organos", "Ladron Organos", "Ladron Organos"]

baraja = [Organo_Rojo, Organo_Azul, Organo_Amarillo, Organo_Verde, Organo_Multicolor,
          Virus_Rojo, Virus_Azul, Virus_Amarillo, Virus_Verde, Virus_Multicolor,
          Medicina_Roja, Medicina_Azul, Medicina_Amarilla, Medicina_Verde, Medicina_Multicolor,
          Transplante, Error_Medico, Guante_Latex, Contagio, Ladron_Organos]

def numero_jugadores():
    global numero_jugadores

    while True:
        numero_jugadores = input("Introduce número de jugadores (de 1 a 6): ")

        if numero_jugadores.isdigit():
            numero_jugadores = int(numero_jugadores)

            if 1 <= numero_jugadores <= 6:
                return numero_jugadores

        print("Número de jugadores no válido, inténtalo de nuevo.")

def barajar(num_pl):

    for i in range(1, num_pl + 1):
        for x in range(0, 3):
            while True:
                try:
                    lista_elegida = random.choice(baraja)
                    if not lista_elegida:
                        continue  # Si la lista está vacía, continúa con la siguiente iteración
                    else:
                        valor = random.choice(lista_elegida)
                        idx = lista_elegida.index(valor)
                        del lista_elegida[idx]

                        if (i == 1):
                            mano_pl1.append(valor)
                        if (i == 2):
                            mano_pl2.append(valor)
                        if (i == 3):
                            mano_pl3.append(valor)
                        if (i == 4):
                            mano_pl4.append(valor)
                        if (i == 5):
                            mano_pl5.append(valor)
                        if (i == 6):
                            mano_pl6.append(valor)
                        break  # Sal del bucle si se selecciona una lista no vacía
                except IndexError:
                    continue

def run(num_pl):
    global num_descartes
    global reintento
    global turno_jugador

    for i in range(1, num_pl + 1):
        if ganador == 1:
            break

        print(" ")
        imprime_tablero()
        print(" ")

        if (i == 1):
            turno_jugador = 1
            print("Mano Jugador 1", mano_pl1)

            while True:
                sel = input("0:Descartar, 1:Jugar Carta, 2:Pasa Turno      ")
                if sel.isnumeric():
                    sel = int(sel)
                    if 0 <= sel <= 2:
                        if (sel == 0):
                            print("Descartar")
                            descartar(mano_pl1)
                            robar(mano_pl1, num_descartes)
                            num_descartes = 0
                            break
                        if (sel == 1):
                            print("Jugar Carta")
                            if Jugar_Carta(mano_pl1, mesa_pl1) == 1:
                                Jugar_Carta(mano_pl1, mesa_pl1)
                                break
                            else:
                                break
                        if (sel == 2):
                            print("Jugador 1 pasa turno")
                            break
                    else:
                        print("El número debe estar en el rango de 0 a 2. inténtalo de nuevo.")
                else:
                    print("El número debe estar en el rango de 0 a 2. inténtalo de nuevo.")

        if (i == 2):
            turno_jugador = 2
            print("Mano Jugador 2", mano_pl2)

            while True:
                sel = input("0:Descartar, 1:Jugar Carta, 2:Pasa Turno      ")
                if sel.isnumeric():
                    sel = int(sel)
                    if 0 <= sel <= 2:
                        if (sel == 0):
                            print("Descartar")
                            descartar(mano_pl2)
                            robar(mano_pl2, num_descartes)
                            num_descartes = 0
                            break
                        if (sel == 1):
                            print("Jugar Carta")
                            if Jugar_Carta(mano_pl2, mesa_pl2) == 1:
                                Jugar_Carta(mano_pl2, mesa_pl2)
                                break
                            else:
                                break
                        if (sel == 2):
                            print("Jugador 2 pasa turno")
                            break
                    else:
                        print("El número debe estar en el rango de 0 a 2. inténtalo de nuevo.")
                else:
                    print("El número debe estar en el rango de 0 a 2. inténtalo de nuevo.")

        if (i == 3):
            turno_jugador = 3
            print("Mano Jugador 3", mano_pl3)

            while True:
                sel = input("0:Descartar, 1:Jugar Carta, 2:Pasa Turno      ")
                if sel.isnumeric():
                    sel = int(sel)
                    if 0 <= sel <= 2:
                        if (sel == 0):
                            print("Descartar")
                            descartar(mano_pl3)
                            robar(mano_pl3, num_descartes)
                            num_descartes = 0
                            break
                        if (sel == 1):
                            print("Jugar Carta")
                            if Jugar_Carta(mano_pl3, mesa_pl3) == 1:
                                Jugar_Carta(mano_pl3, mesa_pl3)
                                break
                            else:
                                break
                        if (sel == 2):
                            print("Jugador 3 pasa turno")
                            break
                    else:
                        print("El número debe estar en el rango de 0 a 2. inténtalo de nuevo.")
                else:
                    print("El número debe estar en el rango de 0 a 2. inténtalo de nuevo.")

        if (i == 4):
            turno_jugador = 4
            print("Mano Jugador 4", mano_pl4)

            while True:
                sel = input("0:Descartar, 1:Jugar Carta, 2:Pasa Turno      ")
                if sel.isnumeric():
                    sel = int(sel)
                    if 0 <= sel <= 2:
                        if (sel == 0):
                            print("Descartar")
                            descartar(mano_pl4)
                            robar(mano_pl4, num_descartes)
                            num_descartes = 0
                            break
                        if (sel == 1):
                            print("Jugar Carta")
                            if Jugar_Carta(mano_pl4, mesa_pl4) == 1:
                                Jugar_Carta(mano_pl4, mesa_pl4)
                                break
                            else:
                                break
                        if (sel == 2):
                            print("Jugador 4 pasa turno")
                            break
                    else:
                        print("El número debe estar en el rango de 0 a 2. inténtalo de nuevo.")
                else:
                    print("El número debe estar en el rango de 0 a 2. inténtalo de nuevo.")

        if (i == 5):
            turno_jugador = 5
            print("Mano Jugador 5", mano_pl5)

            while True:
                sel = input("0:Descartar, 1:Jugar Carta, 2:Pasa Turno      ")
                if sel.isnumeric():
                    sel = int(sel)
                    if 0 <= sel <= 2:
                        if (sel == 0):
                            print("Descartar")
                            descartar(mano_pl5)
                            robar(mano_pl5, num_descartes)
                            num_descartes = 0
                            break
                        if (sel == 1):
                            print("Jugar Carta")
                            if Jugar_Carta(mano_pl5, mesa_pl5) == 1:
                                Jugar_Carta(mano_pl5, mesa_pl5)
                                break
                            else:
                                break
                        if (sel == 2):
                            print("Jugador 5 pasa turno")
                            break
                    else:
                        print("El número debe estar en el rango de 0 a 2. inténtalo de nuevo.")
                else:
                    print("El número debe estar en el rango de 0 a 2. inténtalo de nuevo.")

        if (i == 6):
            turno_jugador = 6
            print("Mano Jugador 6", mano_pl6)

            while True:
                sel = input("0:Descartar, 1:Jugar Carta, 2:Pasa Turno      ")
                if sel.isnumeric():
                    sel = int(sel)
                    if 0 <= sel <= 2:
                        if (sel == 0):
                            print("Descartar")
                            descartar(mano_pl6)
                            robar(mano_pl6, num_descartes)
                            num_descartes = 0
                            break
                        if (sel == 1):
                            print("Jugar Carta")
                            if Jugar_Carta(mano_pl6, mesa_pl6) == 1:
                                Jugar_Carta(mano_pl6, mesa_pl6)
                                break
                            else:
                                break
                        if (sel == 2):
                            print("Jugador 6 pasa turno")
                            break
                    else:
                        print("El número debe estar en el rango de 0 a 2. inténtalo de nuevo.")
                else:
                    print("El número debe estar en el rango de 0 a 2. inténtalo de nuevo.")

def descartar(mano):
    global num_descartes
    long_mano = len(mano)

    for i in range(long_mano):
        if i == 0:
            while True:
                descarte = input("¿Qué carta quieres descartar? Escribe el número de carta (primera 0, segunda 1 ...): ")
                if descarte.isdigit():
                    descarte = int(descarte)
                    if 0 <= descarte < len(mano):
                        mazo_descartes.append(mano[descarte])
                        del mano[descarte]
                        print(mano)
                        num_descartes += 1
                        break
                    else:
                        print("Número de carta fuera de rango, inténtalo de nuevo")
                else:
                    print("Entrada no válida, inténtalo de nuevo")

        else:
            descarte = input("¿Quieres seguir descartando? Escribe s/n: ")
            if descarte.lower() == 's':
                print(mano)
                while True:
                    descarte = input("¿Qué carta quieres descartar? Escribe el número de carta (primera 0, segunda 1 ...): ")
                    if descarte.isdigit():
                        descarte = int(descarte)
                        if 0 <= descarte < len(mano):
                            mazo_descartes.append(mano[descarte])
                            del mano[descarte]
                            num_descartes += 1
                            break
                        else:
                            print("Número de carta fuera de rango, inténtalo de nuevo")
                    else:
                        print("Entrada no válida, inténtalo de nuevo")
            else:
                break

def robar(mano, n_cartas):
    for i in range(n_cartas):
        while True:
            try:
                lista_elegida = random.choice(baraja)
                if not lista_elegida:
                    continue  # Si la lista está vacía, continúa con la siguiente iteración
                else:
                    valor = random.choice(lista_elegida)
                    idx = lista_elegida.index(valor)
                    del lista_elegida[idx]
                    mano.append(valor)
                    break  # Sal del bucle si se selecciona una lista no vacía
            except IndexError:
                continue

    print(mano)

def imprime_tablero():
    Ascii_Art.Espacios()
    print("***************TABLERO****************")
    for i in range(1, numero_jugadores + 1):
        if (i == 1):
            if not mesa_pl1:
                print("")
            else:
                print("Jugador 1 en mesa ", mesa_pl1)
        if (i == 2):
            if not mesa_pl2:
                print("")
            else:
                print("Jugador 2 en mesa ", mesa_pl2)
        if (i == 3):
            if not mesa_pl3:
                print("")
            else:
                print("Jugador 3 en mesa ", mesa_pl3)
        if (i == 4):
            if not mesa_pl4:
                print("")
            else:
                print("Jugador 4 en mesa ", mesa_pl4)
        if (i == 5):
            if not mesa_pl5:
                print("")
            else:
                print("Jugador 5 en mesa ", mesa_pl5)
        if (i == 6):
            if not mesa_pl6:
                print("")
            else:
                print("Jugador 6 en mesa ", mesa_pl6)
    print("**************************************")

def Jugar_Carta(mano, mesa):
    sel = input("0:Virus, 1:Medicina, 2:Tratamiento, 3:Lanzar Organo, 4:Pasar Turno      ")
    org = []
    med = []
    n_org = 0
    n_med = 0
    estado_org = 0
    i_next = 0

    if(sel == '0'):
        print("Virus")

    if(sel == '1'):
        print("Medicina")
        if(Busca_Texto_Mano(mano,"Medicina")==1):
            if(Busca_Texto_Mano(mesa, "Organo")):
                if(i_next==0):
                    while True:
                        print(mano)
                        med = input("Selecciona la medicina a emplear, Escribe el número de carta (primera 0, segunda 1 ...):   ")
                        if med.isnumeric():
                            med = int(med)
                            if (med <= len(mano)):
                                if (Busca_Texto(mano[med], "Medicina") == 1):
                                    i_next = 1
                                    break
                                else:
                                    print("No has seleccionado una medicina")
                            else:
                                print("Entrada no válida")
                        else:
                            print("Entrada no válida")
                if(i_next==1):
                    while True:
                        print(mesa)
                        org = input("Selecciona el organo a curar, Escribe el número de carta (primera 0, segunda 1 ...):   ")
                        if org.isnumeric():
                            org = int(org)
                            if (org <= len(mesa)):
                                if (Busca_Texto(mesa[org], "Organo") == 1):
                                    i_next = 2
                                    break
                                else:
                                    print("No has seleccionado una organo")
                            else:
                                print("Entrada no válida")
                        else:
                            print("Entrada no válida")
                if(i_next==2):
                    #Organo multicolor
                    if (Busca_Texto(mesa[org], "Organo Multicolor")):
                        estado_org = Estado_Organo(mesa[org])

                        if (estado_org == 0):  # Sano
                            mesa[org] += "+"
                            del mano[med]
                            robar(mano, 1)

                        if (estado_org == 1):  # Vacunado
                            mesa[org] += "+"
                            del mano[med]
                            robar(mano, 1)

                        if (estado_org == 2):  # Inmunizado
                            print("Organo inmunizado, no puedes usar la medicina")
                            return 1
                    else:
                        i_next = 3
                if(i_next==3):
                    #Medicina multicolor
                    if (Busca_Texto(mano[med], "Medicina Multicolor")):
                        estado_org = Estado_Organo(mesa[org])

                        if (estado_org == 0):  # Sano
                            mesa[org] += "+"
                            del mano[med]
                            robar(mano, 1)

                        if (estado_org == 1):  # Vacunado
                            mesa[org] += "+"
                            del mano[med]
                            robar(mano, 1)

                        if (estado_org == 2):  # Inmunizado
                            print("Organo inmunizado, no puedes usar la medicina")
                            return 1
                    else:
                        i_next = 4
                if(i_next==4):
                    #Color Organo = Color Medicina
                    if(Compara_Color(mesa[org], mano[med])==1):
                        estado_org = Estado_Organo(mesa[org])

                        if (estado_org == 0):  # Sano
                            mesa[org] += "+"
                            del mano[med]
                            robar(mano, 1)

                        if (estado_org == 1):  # Vacunado
                            mesa[org] += "+"
                            del mano[med]
                            robar(mano, 1)

                        if (estado_org == 2):  # Inmunizado
                            print("Organo inmunizado, no puedes usar la medicina")
                            return 1
                    else:
                        return 1
            else:
                print("No dispones de organos en mesa")
                return 1
        else:
            print("No dispones medicinas")
            return 1

    if(sel == '2'):
        print("Tratamiento")

    if(sel == '3'):
        print("Lanzar Organo")
        if(Busca_Texto_Mano(mano, "Organo")==1):
            while True:
                print(mano)
                org = input("Selecciona el organo a lanzar, Escribe el número de carta (primera 0, segunda 1 ...):   ")
                if org.isnumeric():
                    org = int(org)
                    if(Busca_Texto(mano[org], "Organo") == 1):
                        if (org <= len(mano)):
                            mesa.append(mano[org])
                            del mano[org]
                            robar(mano, 1)
                            Comprueba_Ganador(mesa)
                            break
                    else:
                        print("No has seleccioando un órgano")
                else:
                    print("Entrada no válida")
        else:
            print("no tienes organos que jugar")
            return 1

    if(sel == '4'):
        print("Pasaste Turno")


def Busca_Texto_Mano(mano, palabra):
        encontrado = False

        for item in mano:
            if palabra in item.split():
                encontrado = True
                break
        if encontrado:
            return 1    #Texto Encontrado
        else:
            return 0    #Texto No Encontrado

def Busca_Texto(cadena, palabra):
    indice = cadena.find(palabra)
    if indice != -1:
        return 1
    else:
        return 0

def Compara_Color(cadena1, cadena2):
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()

    colores = ["roj", "amarill", "verde", "azul", "multicolor"]

    for color in colores:
        if color in cadena1 and color in cadena2:
            return 1    #coinciden

    return 0    #no coinciden

def Estado_Organo(Organo):
    if "++" in Organo:
        return 2
    elif "*" in Organo:
        return 3
    else:
        return 1 if "+" in Organo else 0

def Comprueba_Ganador(Mesa):
    global ganador
    global turno_jugador

    n_ganar = 0

    if "Organo Rojo" in Mesa or "Organo Rojo+" in Mesa or "Organo Rojo++" in Mesa:
        n_ganar = n_ganar + 1
    if "Organo Amarillo" in Mesa or "Organo Amarillo+" in Mesa or "Organo Amarillo++" in Mesa:
        n_ganar = n_ganar + 1
    if "Organo Verde" in Mesa or "Organo Verde+" in Mesa or "Organo Verde++" in Mesa:
        n_ganar = n_ganar + 1
    if "Organo Azul" in Mesa or "Organo Azul+" in Mesa or "Organo Azul++" in Mesa:
        n_ganar = n_ganar + 1
    if "Organo Multicolor" in Mesa or "Organo Multicolor+" in Mesa or "Organo Multicolor++" in Mesa:
        n_ganar = n_ganar + 1

    if n_ganar == 4:
        # imprime_tablero()
        # print(" ")
        # print("FIN Juego!! ganador Jugador " + str(turno_jugador))
        ganador = 1



Ascii_Art.Intro()
numero_jugadores()
barajar(numero_jugadores)

while ganador<1:
    run(numero_jugadores)

while ganador == 1:
    if (ganador_texto == 0):
        print(" ")
        imprime_tablero()
        print(" ")
        print("FIN del juego!! ganador Jugador " + str(turno_jugador))
        ganador_texto = 1
