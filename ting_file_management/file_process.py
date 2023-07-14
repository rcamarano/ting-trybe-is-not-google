import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    origin_file = txt_importer(path_file)
    result_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(origin_file),  # type: ignore
        "linhas_do_arquivo": origin_file,
    }
    instance.enqueue(result_file)
    sys.stdout.write(f"{result_file}\n")
    return result_file


def remove(instance):
    """Aqui irá sua implementação"""
    # if len(instance) == 0:
    #     sys.stdout.write("Não há elementos\n")
    #     return None

    # file = instance.dequeue()
    # sys.stdout.write(
    #     f"Arquivo {file['nome_do_arquivo']} removido com sucesso\n"
    # )
    # return file


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    # if position < 0 or position >= len(instance):
    #     sys.stderr.write("Posição inválida\n")
    #     return None

    # file = instance.search(position)
    # sys.stdout.write(f"{file}\n")
    # return
