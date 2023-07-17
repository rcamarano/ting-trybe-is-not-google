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
    words_foud = []

    for file_content in instance._list:
        file_name = file_content["nome_do_arquivo"]
        times_apeared = []

        for line_number, line_content in enumerate(
            file_content["linhas_do_arquivo"], start=1
        ):
            if word.lower() in line_content.lower():
                incidence = {"linha": line_number, "conteudo": line_content}
                times_apeared.append(incidence)

        if times_apeared:
            result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": times_apeared,
            }
            words_foud.append(result)

    return words_foud
