
from nodo import Nodo

class DoublyLinkedList:
    def __init__(self):
        # head = la cabeza de la lista, primer dato de la lista
        self.head = None
        # tail = el final de la lista , ultimo dato de la lista
        self.tail = None
        # size = para llevar el tamaño de la lista
        self.size = 0

    @property
    # metodo first para verificar si hay algun dato en la cabeza de la lista
    # si no hay nada , lanza un mensaje que dice que la lista esta vacia
    def first(self) -> Nodo:
        if self.is_empty():
            raise Exception('Lista vacía')
        else:
            return self.head

    @property
    # metodo last para verificar si hay algun dato al final de la lista
    def last(self) -> Nodo:
        if self.is_empty():
            raise Exception('Lista vacía')
        else:
            return self.tail

    # metodo que devuelve el tamaño de la lista
    def __len__(self) -> int:
        return self.size

    # verificar si la lista esta vacía
    def is_empty(self) -> bool:
        return self.size == 0 and self.head is None and self.tail is None

    # Recorre la lista
    def traversal(self) -> str:
        result = ''
        if self.is_empty() is False:
            current = self.head
            grado = self.size - 1
            while current is not self.tail:
                signo = "+" if current.data > 0 else ""
                result += signo + str(current.data) + f"x^{grado} "
                current = current.next
                grado -= 1
            signo = "+" if self.tail.data > 0 else ""
            result += signo + str(self.tail.data)
        return result

    # insertar al inicio
    def prepend(self, data) -> None:
        new_node = Nodo(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1


    # remover al final - devuelve data
    def pop(self):
        if self.is_empty():
            raise Exception('The list is empty')
        elif self.size == 1:
            current = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return current.data
        else:
            current = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            current.prev = None
            self.size -= 1
            return current.data


