from lista_circular_doble import DoublyLinkedList

# lista que guardara los elementos del polinomio A
a: DoublyLinkedList = DoublyLinkedList()
# lista que guardara los elementos del polinomio B
b: DoublyLinkedList = DoublyLinkedList()
# lista que guardara el polinomio resultante de las operaciones
c: DoublyLinkedList = DoublyLinkedList()

a.prepend(-10)
a.prepend(18)
a.prepend(3)
b.prepend(-25)
b.prepend(0)
b.prepend(4)
b.prepend(-17)

# Primer parcial María Esther Tigüilá Soloj - 1627021
while True:
    print("\n")
    print("------BIENVENIDO-----")
    print("Menu principal:")
    print('POLINOMIOS')
    print('\nAcciones:')
    print('1- Ingresar componentes a un polinomio  ')
    print('2- Adicion y sustracción  ')
    print('3- Evaluar polinomios')
    print('4- Salir.')
    opcion = int(input('Seleccione una acción: '))
    if opcion == 1:
        print('Estado del polinomio actual: ')
        print('polinomio A ', a.traversal())
        print('polinomio B ', b.traversal())
        print('A que polinomio desea agregar un componente ')
        print('1- polinomio  A')
        print('2- polinomio B')
        print('3- regresar al menu principal ')
        opcion = int(input('selecione una opcion '))
        if opcion == 1:
            data = int(input('Ingrese el coeficiente del polinomio y su signo - o +: '))
            # agrega el coeficiente al inicio de la lista
            a.prepend(data)
            print('Estado del polinomio A: ', a.traversal())
            # muestra y recorre el estado del polinomio
            size = len(a)
            print('Grado del polinomio: ', size)

        elif opcion == 2:
            data = int(input('Ingrese el coeficiente del polinomio y su signo - o +: '))
            b.prepend(data)
            print('Estado del polinomio B: ', b.traversal())
            size = len(b)
            print('Grado del polinomio: ', size)
        elif opcion == 3:
            print('regresando al menu..')
            break
        else:
            continue
    elif opcion == 2:
        print('Que opcion desea realizar ')
        print('1- suma')
        print('2- resta')
        print('3 - regresar al menu ')
        opcion = int(input('Seleccione una accion '))
        if opcion == 1:
            c: DoublyLinkedList = DoublyLinkedList()
            if len(a) >= len(b):
                # polinomio a es mas grande
                while len(a) > 0:
                    n1 = a.pop()
                    n2 = b.pop()
                    c.prepend(n1 + n2)
                while len(b) > 0:
                    n1 = a.pop()
                    c.prepend(n1)
            else:
                while len(a) > 0:
                    n1 = a.pop()
                    n2 = b.pop()
                    c.prepend(n1 + n2)
                while len(b) > 0:
                    n1 = b.pop()
                    c.prepend(n1)
            print('c = ', c.traversal())
        elif opcion == 2:
            c: DoublyLinkedList = DoublyLinkedList()
            if len(a) >= len(b):
                # polinomio a es mas grande
                while len(a) > 0:
                    n1 = a.pop()
                    n2 = b.pop()
                    c.prepend(n1 - n2)
                while len(b) > 0:
                    n1 = a.pop()
                    c.prepend(n1)
            else:
                while len(a) > 0:
                    n1 = a.pop()
                    n2 = b.pop()
                    c.prepend(n1 - n2)
                while len(b) > 0:
                    n1 = b.pop()
                    c.prepend(n1)
            print('c = ', c.traversal())
        elif opcion == 3:
            print('regresando al menu...')
            break
        else:
            continue

    elif opcion == 3:
        print('Cual polinomio desea Evaluar')
        print('1- polinomio A: ', {a.traversal()})
        print('2- polinomio B: ', {b.traversal()})
        print('3 - regresar al menu ')
        opcion = int(input('Seleccione una accion '))
        if opcion == 1:
            variable = int(input('Ingrese el valor para la variable desconocida (X): '))
            grado = 0
            resultado = 0
            while len(a) > 0:
                n1 = a.pop()
                resultado += n1 * (variable ** grado)
                grado += 1
            print(resultado)
        elif opcion == 2:
            variable = int(input('Ingrese el valor para la variable desconocida (X): '))
            grado = 0
            resultado = 0
            while len(a) > 0:
                n1 = b.pop()
                resultado += n1 * (variable ** grado)
                grado += 1
            print(resultado)
        elif opcion == 3:
            print('regresando al menu...')
            break
        else:
            continue

    elif opcion == 4:
        print('Saliendo....')
        break
    else:
        continue
#