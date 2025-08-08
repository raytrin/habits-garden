import json
from modulos.utilidades import validar_data_metas

ARQUIVO_METAS = "dados/metas.json"

def carregar_metas():
    """Carrega as metas salvas"""
    try:
        with open(ARQUIVO_METAS, "r", encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_metas(metas):
    """Salva as metas no arquivo json"""
    with open(ARQUIVO_METAS, "w", encoding='utf-8') as arquivo:
        json.dump(metas, arquivo, indent=2)

#---------------------------------------------------- adicionar metas -----------------------------------------------
def adicionar_metas(nome, periodo, tempo):
    """Salva as metas no arquivo json"""
    metas = carregar_metas()

    nova_meta = {
        "nome": nome,
        "tempo": tempo
    }

    #verifica se o período semanal já existe para adicionar a nova meta no mesmo período
    periodo_existente = False
    for semana in metas:
        if semana["periodo"] == periodo:
            semana["metas"].append(nova_meta)
            periodo_existente = True
            break

    #adiciona a nova meta no novo período
    if not periodo_existente:
        nova_semana = {
            "periodo": periodo,
            "metas": [nova_meta]
        }
        metas.append(nova_semana)

    salvar_metas(metas)
    return True, f"Meta {nome} adicionada com sucesso para o período {periodo}!"

#---------------------------------------------- editar metas por índice ----------------------------------------------
def editar_metas_por_indice(indice, data, novo_nome, novo_tempo):
    """Permite editar uma meta existente, atualizando nome e tempo. Retorna uma mensagem indicando o resultado da operação."""

    metas = carregar_metas()

    for meta in metas:
        if meta["periodo"] == data:
            metas_da_semana = meta["metas"]

            if not novo_nome or not novo_tempo:
                return False, "Por favor, preencha todos os campos."

            if indice < 0 or indice >= len(metas_da_semana):
                return False, "Índice inválido para edição."

            metas_da_semana[indice]["nome"] = novo_nome
            metas_da_semana[indice]["tempo"] = novo_tempo

            salvar_metas(metas)

            return True, f"Meta editada com sucesso!"

    return False, "Nenhuma meta encontrada."
#------------------------------------------------- excluir metas -------------------------------------------------
def excluir_metas_por_indice(data, indice):
    """Recebe uma lista de metas, filtra as metas com a data informada, usa o índice para selecionar a meta individual que deverá ser excluída."""

    metas = carregar_metas()

    for meta in metas:
        if meta.get("periodo") == data:
            metas_da_semana = meta.get("metas", [])

            if indice < 0 or indice >= len(metas_da_semana):
                return f"Indice inválido."

            metas_da_semana.pop(indice)
            salvar_metas(metas)
            return True, "Meta excluída com sucesso."

    return False, "A meta não pode ser excluída."
#-------------------------------------------------- excluir periodo ---------------------------------------------------
def excluir_metas_por_periodo(data):
    """Recebe uma lista com as metas, filtra as metas com a data informada e armazena em uma nova lista para ser excluída permanentemente. """
    metas = carregar_metas()

    #armazena metas do período informado para futura exclusão
    metas_exclusao = []

    for meta in metas:
        if meta["periodo"] == data:
            metas_exclusao.append(meta)

    #remove da lista principal todas as metas do período informado
    for meta in metas_exclusao:
        metas.remove(meta)
    salvar_metas(metas)
    return True, "Período excluído com sucesso."

#--------------------------------------------------- selecionar tarefas -----------------------------------------------
def seleciona_metas(data):
    """Recebe uma lista de metas, valida a data informada, filtra as metas com a data informada e retorna uma lista de metas correspondentes para o período."""
    sucesso, data_inicio, data_fim = validar_data_metas(data)

    if not sucesso:
        return False, "Verifique a data informada."


    metas = carregar_metas()
    for semana in metas:
        if semana["periodo"] == data:
            metas_do_dia = semana["metas"]
            if not metas_do_dia:
                return False, f"Nenhuma meta encontrada para essa data."

            return True, metas_do_dia

