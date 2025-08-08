import datetime as dt
from modulos.registro import carregar_tarefas
from modulos.metas import carregar_metas
from modulos.utilidades import formatar_tempo, validar_data_metas, semana_atual

def gerar_relatorio(periodo):
    """Recebe a lista de metas e tarefas, verifica se existem metas e tarefas para o período informado,
    conta o tempo gasto em cada atividade do período e compara com a meta estabelecida para aquela atividade,
    retornando um relatório das metas que foram e não foram atingidas, bem como a frequência semanal das atividades."""

    tarefas = carregar_tarefas()
    metas = carregar_metas()

    if not metas:
        return "Nenhuma meta encontrada."

    if not tarefas:
        return "Nenhuma tarefa encontrada."

    #procura o período informado
    metas_da_semana = None
    for meta in metas:
        if meta.get("periodo") == periodo:
            metas_da_semana = meta.get("metas", [])
            break

    if metas_da_semana is None:
        return "Período não encontrado."

    if not metas_da_semana:
        return f"Nenhuma meta encontrada para este período."

    #transforma o período inserido em data
    sucesso, data_inicio, data_fim = validar_data_metas(periodo)

    tarefas_da_semana = []
    if sucesso:
        #procura as tarefas da semana através das datas
        for dia in tarefas:
            try:
                data = dt.datetime.strptime(dia["data"], "%d/%m/%Y").date()
            except (ValueError, KeyError):
                continue

            if data_inicio <= data <= data_fim:
                tarefas_da_semana.extend(dia["tarefas"])

    if not tarefas_da_semana:
        return "Nenhuma tarefa encontrada para esse período"

    tempo_total_tarefas = {}
    contagem_tarefas = {}

    #verifica o tempo total inserido para cada tarefa da semana e a frequência
    for tarefa in tarefas_da_semana:
        nome_tarefa = tarefa["nome"].strip().lower()
        tempo_tarefa = tarefa["tempo"]

        if nome_tarefa in tempo_total_tarefas:
            tempo_total_tarefas[nome_tarefa] += tempo_tarefa
            contagem_tarefas[nome_tarefa] += 1
        else:
            tempo_total_tarefas[nome_tarefa] = tempo_tarefa
            contagem_tarefas[nome_tarefa] = 1

    relatorio = []

    #cria o relatório comparando dados de metas e tarefas
    for meta in metas_da_semana:
        nome_meta = meta["nome"].strip().lower()
        tempo_meta = meta["tempo"]
        tempo_realizado = tempo_total_tarefas.get(nome_meta, 0)

        porcentagem = (tempo_realizado / tempo_meta) * 100
        porcentagem = round(porcentagem, 2)

        meta_atingida = tempo_realizado >= tempo_meta
        status = "💎 Mais uma vitória sua! Você está construindo uma versão incrível de si!" if meta_atingida else "🌸 Progresso não é perfeição. Você está evoluindo a cada dia!"
        tempo_formatado = formatar_tempo(tempo_realizado)
        tempo_meta_formatado = formatar_tempo(tempo_meta)

        relatorio.append(f"\n📌 Atividade: {nome_meta.capitalize()}")
        relatorio.append(f"🎯 Meta: {tempo_meta_formatado.capitalize()}.")
        relatorio.append(f"🔁 Frequência: {contagem_tarefas.get(nome_meta, 0)}x na semana.")
        relatorio.append(f"⏰ Você realizou: {tempo_formatado}.")
        relatorio.append(f"📈 Progresso: {porcentagem}%.")
        relatorio.append(f" Status: {status}")

    return "\n".join(relatorio)

def gerar_dados_grafico():
    """Compara a meta com o tempo total realizado para cada atividade. Retorna uma lista com um dicionário para cada atividade. """

    periodo_atual, inicio_semana, fim_semana = semana_atual()
    metas = carregar_metas()
    tarefas = carregar_tarefas()
    dados_grafico = []

    todas_metas = []
    for meta_periodo in metas:
        if meta_periodo["periodo"] == periodo_atual:
            todas_metas.extend(meta_periodo["metas"])

    for meta in todas_metas:
        nome_meta = meta["nome"]
        tempo_meta = meta["tempo"]
        tempo_total = 0

        #usando o try para ignorar entradas mal formatadas e não quebrar
        #seleciona as tarefas da semana comparando a data informada com a data de início e fim da semana atual
        for dia in tarefas:
            try:
                data = dt.datetime.strptime(dia["data"], "%d/%m/%Y").date()
            except (ValueError, KeyError):
                continue
            if inicio_semana <= data <= fim_semana:
                for tarefa in dia["tarefas"]:
                    if tarefa["nome"].strip().lower() == nome_meta.strip().lower():
                        tempo_total += int(tarefa["tempo"])

        dados_grafico.append({
            "Atividade": nome_meta.title(),
            "Meta": tempo_meta,
            "Realizado": tempo_total
        })

    return dados_grafico





