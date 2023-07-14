import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith('.txt'):
        print("Formato inválido", file=sys.stderr)
        return []
    try:
        with open(path_file, 'r', encoding='utf+8') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []
