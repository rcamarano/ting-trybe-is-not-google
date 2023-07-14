from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.list = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.list)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        return self.list.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.list.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index >= len(self.list):
            raise IndexError("Index inválido ou Inexistente")
