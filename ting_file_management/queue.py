from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._list = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._list)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        return self._list.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if len(self._list) == 0:
            return None
        else:
            return self._list.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index >= len(self._list):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._list[index]
