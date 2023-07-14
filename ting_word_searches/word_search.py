def exists_word(word, instance):
    """Aqui irá sua implementação, vamos começar"""
    files_base = [
        {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": line}
                for line, line_content in enumerate(
                    file["linhas_do_arquivo"], start=1
                )
                if word.lower() in line_content.lower()
            ],
        }
        for file in instance._list
        if any(
            word.lower() in line_content.lower()
            for line_content in file["linhas_do_arquivo"]
        )
    ]

    return files_base


def search_by_word(word, instance):
    """Aqui irá sua implementação, VQV!"""
