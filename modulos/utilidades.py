import datetime as dt
import random

def validar_data(data):
    """Verifica se a data inserida está no formato correto de dia/mês/ano. Retorna True ou False e a data no formato datetime."""

    try:
        data_formatada = dt.datetime.strptime(data, '%d/%m/%Y')
        return True, data_formatada
    except ValueError:
        return False, "Data inválida. Use o formato dd/mm/aaaa."
# --------------------------------------------------- validar tempo -------------------------------------------------
def validar_tempo(tempo):
    """Valida se o tempo é maior do que zero."""

    return tempo > 0
# ---------------------------------------------------- formatar tempo -----------------------------------------------
def formatar_tempo(minutos):
    """Recebe o tempo em minutos e retorna o tempo formatado em horas e minutos. Se o tempo for menor que 60 minutos, retorna apenas os minutos."""
    try:
        minutos = int(minutos)
        horas = minutos // 60
        minutos = minutos % 60
        if horas == 0:
            return f"{minutos} min"
        elif minutos == 0:
            return f"{horas}h"
        else:
            return f"{horas} horas e {minutos} minutos"
    except ValueError:
        return "Digite um número válido"
# -------------------------------------------------- mostrar frases -------------------------------------------------
def mostra_frases():
    """Seleciona frases aleatórias de um arquivo txt para serem mostradas na tela inicial do app.py"""

    frases = "modulos/quotes.txt"
    try:
        with open(frases, "r", encoding='utf-8') as arquivo:
            frases = arquivo.readlines()
            frases_aleatorias = random.choice(frases)
            return frases_aleatorias
    except FileNotFoundError:
        return None
# ------------------------------------------------ validar periodo das metas -----------------------------------------
def validar_data_metas(data):
    """Transforma a string do período das metas em data e retorna True ou False, e a data no formato (data_inicio, data_fim)"""
    try:
        data_inicio, data_fim = data.split(" - ")
        ano_atual = dt.datetime.now().year
        data_inicio = dt.datetime.strptime(f"{data_inicio}/{ano_atual}", "%d/%m/%Y").date()
        data_fim = dt.datetime.strptime(f"{data_fim}/{ano_atual}", "%d/%m/%Y").date()
        return True, data_inicio, data_fim
    except ValueError:
        return False, None, "Data inválida. Use o formato dd/mm - dd/mm"

# ---------------------------------------------- encontrar a semana atual --------------------------------------------
def semana_atual():
    """Usa o módulo time para encontrar a semana atual e retorna o período para as metas, a data do início da semana e a data do fim da semana."""

    hoje = dt.date.today()
    try:
        inicio_semana = hoje - dt.timedelta(days=hoje.weekday())
        fim_semana = inicio_semana + dt.timedelta(days=6)

        periodo = f"{inicio_semana.strftime('%d/%m')} - {fim_semana.strftime('%d/%m')}"
        return periodo, inicio_semana, fim_semana
    except ValueError:
        return False, "Erro ao encontrar a semana atual."