import json
from modulos.utilidades import validar_data


ARQUIVO_TAREFAS = "dados/tarefas.json"

def carregar_tarefas():
    """Carrega as tarefas salvas"""
    try:
        with open(ARQUIVO_TAREFAS, "r", encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_tarefas(tarefas):
    """Salva as tarefas no arquivo json"""

    with open(ARQUIVO_TAREFAS, "w", encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=2)

# ----------------------------------------------- adicionar tarefa --------------------------------------------------
def adicionar_tarefa(data, categoria, nome, tempo, observacao=""):
    """Recebe uma lista de tarefas. Verifica se a data informada já existe, adiciona os novos dados à data informada.
    Caso não exista, adiciona uma nova data para os novos dados."""

    #verifica se a data foi inserida no formato correto
    if not validar_data(data):
        return  False, f"Data inválida! Use o formato dd/mm/aaaa."

    tarefas = carregar_tarefas()

    nova_tarefa = {
        "categoria": categoria,
        "nome": nome,
        "tempo": tempo,
        "observacao": observacao,
    }

    #se a data existir, adiciona nova tarefa para o dia
    data_encontrada = False
    for dia in tarefas:
        if dia["data"] == data:
            dia["tarefas"].append(nova_tarefa)
            data_encontrada = True
            break

    #se a data não existir, cria data e adiciona as tarefas do dia
    if not data_encontrada:
        novo_dia = {
            "data": data,
            "tarefas": [nova_tarefa]
        }
        tarefas.append(novo_dia)

    salvar_tarefas(tarefas)
    return True, f"Tarefa {nome} adicionada com sucesso!"

# ------------------------------------------------ selecionar tarefa --------------------------------------------------
def seleciona_tarefas(data):
    """Seleciona as tarefas que serão editadas. Retorna uma lista de tarefas."""

    sucesso, mensagem = validar_data(data)
    if not sucesso:
        return False, mensagem

    dias = carregar_tarefas()

    for dia in dias:
        if dia["data"] == data:
            tarefas_do_dia = dia["tarefas"]
            if not tarefas_do_dia:
                return False, f"Nenhuma tarefa encontrada para essa data."

            return True, tarefas_do_dia

    return False, "Tarefa não encontrada. Verifique a data informada."

#----------------------------------------------- editar tarefa -----------------------------------------------------
def editar_tarefa_por_indice(indice, data, nova_categoria, novo_nome, novo_tempo, nova_observacao = ""):
    """Edita uma tarefa específica"""
    dias = carregar_tarefas()

    for dia in dias:
        if dia["data"] == data:
            tarefas_do_dia = dia["tarefas"]

            tarefas_do_dia[indice]["categoria"] = nova_categoria
            tarefas_do_dia[indice]["nome"] = novo_nome
            tarefas_do_dia[indice]["tempo"] = novo_tempo
            tarefas_do_dia[indice]["observacao"] = nova_observacao

            salvar_tarefas(dias)
            return True, "Tarefa editada com sucesso!"


#------------------------------------------------- excluir tarefa ------------------------------------------------

def excluir_tarefa_por_indice(indice, data):
    """Exclui uma tarefa existente. Localiza a tarefa pela data e número da tarefa informados."""

    dias = carregar_tarefas()

    for dia in dias:
        if dia["data"] == data:
            tarefas_do_dia = dia["tarefas"]

            tarefas_do_dia.pop(indice)
            salvar_tarefas(dias)
            return True, "Tarefa excluída com sucesso!"
