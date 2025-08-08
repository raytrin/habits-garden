import streamlit as st

from modulos.registro import adicionar_tarefa, seleciona_tarefas, editar_tarefa_por_indice, excluir_tarefa_por_indice
from modulos.metas import seleciona_metas, editar_metas_por_indice, excluir_metas_por_indice, adicionar_metas, excluir_metas_por_periodo
from modulos.relatorios import gerar_relatorio, gerar_dados_grafico
from modulos.utilidades import formatar_tempo, mostra_frases


st.set_page_config(page_title="Habit's Garden", layout="centered", page_icon="🌷")
st.markdown(
    "<h1 style='text-align: center;'>🌷 Habit's Garden 🌷</h1>",
    unsafe_allow_html=True)

menu = st.sidebar.selectbox("🌸 Escolha uma opção 🌸", ["Página Inicial", "Ver Tarefas", "Adicionar Tarefas", "Excluir Tarefas", "Editar Tarefas", "Ver Metas", "Adicionar Metas", "Editar Metas", "Excluir Metas", "Exibir Relatório"])

#--------------------------------------------------- pagina inicial-------------------------------------------------
if menu == "Página Inicial":


    st.markdown(
        "<h6 style='text-align: center; color: #FFB6C1; '>Cultivando a pessoa que você quer ser, uma semana de cada vez.</h6>",
        unsafe_allow_html=True)

    frases = mostra_frases()
    st.markdown(
        f"<p style='text-align: center; color: #666666; font-size: 14px; font-style: italic;'>✨ {frases}</p>",
        unsafe_allow_html=True
    )

    st.markdown("<hr style='border:1px solid #cccccc'>", unsafe_allow_html=True)
    st.subheader("💐 Progresso da semana:")

    st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-color: #B19CD9;  /* Cor azul */
    }
    </style>
    """, unsafe_allow_html=True)

    dados = gerar_dados_grafico()
    if not dados:
        st.write("📝 Adicione tarefas para ver o progresso da semana.")
    for item in dados:
        progresso = (item['Realizado'] / item['Meta']) * 100
        st.progress(progresso / 100)
        st.write(f"{item['Atividade']}: {progresso:.1f}%")

#-------------------------------------------------- ver tarefas -----------------------------------------------------
if menu == "Ver Tarefas":

    st.subheader("📋 Tarefas do dia")
    data = st.text_input("Digite a data (dd/mm/aaaa):")

    if st.button("🔍 Buscar"):
        sucesso, tarefas = seleciona_tarefas(data)
        if not sucesso:
            st.error(tarefas)
            st.stop()

        st.subheader(f"📅 Tarefas do dia {data}")

        for tarefa in tarefas:
            st.write(f"📌 Nome: {tarefa.get('nome')}")
            st.write(f"📂 Categoria: {tarefa.get('categoria')} ")
            st.write(f"⏰ Tempo: {formatar_tempo(tarefa.get('tempo'))}")
            st.write(f"📝 Observação: {tarefa.get('observacao') or '—'}")
            st.write("---")

#------------------------------------------------- adicionar tarefas ----------------------------------------------
if menu == "Adicionar Tarefas":
    st.subheader("✍️ Adicionar Tarefas")

    with st.form("adicionar_tarefa"):
        data = st.text_input('📅 Digite a data da tarefa (dd/mm/aaaa): ')
        nome = st.text_input('📌 Digite o nome da tarefa: ').strip().lower()
        categoria = st.text_input('📂 Digite a categoria (estudo, leitura, autocuidado, trabalho): ').strip().lower()
        tempo = st.number_input('⏰ Digite o tempo gasto (em minutos): ', min_value=1)
        observacao = st.text_input('📝 Observações (opcional): ').strip().lower()

        enviar = st.form_submit_button("Adicionar")

        if enviar:
            sucesso, mensagem =  adicionar_tarefa(data, categoria, nome, tempo, observacao)
            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)

#------------------------------------------------- editar tarefas --------------------------------------------------
if menu == "Editar Tarefas":
    st.subheader("✏️ Editar Tarefas")
    data = st.text_input("Digite a data da tarefa que deseja editar (dd/mm/aaaa): ").strip()

    if data:
        sucesso, tarefas = seleciona_tarefas(data)
        if not sucesso:
            st.error(tarefas)
            st.stop()

        st.subheader("📋 Tarefas encontradas:")
        for i, tarefa in enumerate(tarefas, start=1):
            st.write(f"✔️ Tarefa - {i} | {tarefa.get('nome', 'sem nome')} | {tarefa.get('categoria', 'sem categoria')} | {tarefa.get('tempo', 0)} minutos | {tarefa.get('observacao', 'sem observação')}")

        with st.form("editar_tarefa"):
            indice = st.number_input("Número da tarefa que deseja editar:", min_value=1, max_value=len(tarefas)) -1
            novo_nome = st.text_input("📌 Novo nome:").strip()
            nova_categoria = st.text_input("📂 Nova categoria:").strip()
            novo_tempo = st.number_input("⏰ Novo tempo (minutos):", min_value=1)
            nova_observacao = st.text_input("📝 Nova observação: ").strip()

            enviar = st.form_submit_button("Confirmar")

            if enviar:
                if not nova_categoria or not novo_nome or not novo_tempo:
                    st.warning("⚠️ Preencha todos os campos.")
                    st.stop()

                sucesso, mensagem = editar_tarefa_por_indice(indice, data, nova_categoria, novo_nome, novo_tempo, nova_observacao)
                if sucesso:
                    st.success(mensagem)
                else:
                    st.error(mensagem)

#-------------------------------------------------- excluir tarefas ------------------------------------------------
if menu == "Excluir Tarefas":

    st.subheader("🗑️ Excluir Tarefas")
    data = st.text_input("Digite a data da tarefa que deseja excluir (dd/mm/aaaa): ").strip()

    if data:
        sucesso, tarefas = seleciona_tarefas(data)

        st.subheader("📋 Tarefas encontradas:")
        for i, tarefa in enumerate(tarefas, start=1):
            st.write(f"✔️ Tarefa {i} - {tarefa.get('nome', 'Sem nome')} | {tarefa.get('categoria', 'Sem categoria')} | {tarefa.get('tempo', 0)} minutos")

        with st.form("excluir_tarefa"):
            indice = st.number_input(f"Digite o número da tarefa que deseja excluir: ", min_value=1, max_value=len(tarefas)) -1

            enviar = st.form_submit_button("Confirmar")
            if enviar:
                sucesso, mensagem = excluir_tarefa_por_indice(indice, data)
                if sucesso:
                     st.success(mensagem)
                else:
                    st.error(mensagem)
                    st.stop()

#-------------------------------------------------- ver metas ------------------------------------------------------
if menu == "Ver Metas":

    st.subheader("📋 Metas da semana")

    data = st.text_input("Digite o período (dd/mm - dd/mm):")
    if st.button("🔍 Buscar"):
        sucesso, metas_do_dia = seleciona_metas(data)
        if not sucesso:
            st.error(metas_do_dia)
            st.stop()

        st.subheader(f"📅 Metas da semana {data}")
        for atividade in metas_do_dia:
            st.write(f"📌 Nome: {atividade.get('nome').capitalize()}")
            st.write(f"⏰ Tempo: {formatar_tempo(atividade.get('tempo'))}")
            st.write("---")
#------------------------------------------------- adicionar metas ---------------------------------------------
if menu == "Adicionar Metas":
    st.subheader("✍️ Adicionar Metas")

    with st.form("adicionar metas"):
        periodo = st.text_input(f"📅 Período (dd/mm - dd/mm):")
        nome = st.text_input("📌 Nome: ").strip()
        tempo = st.number_input("⏰ Tempo (minutos): ", min_value=1)

        confirmar = st.form_submit_button("Confirmar")

        if confirmar:
            sucesso, mensagem = adicionar_metas(nome, periodo, tempo)
            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)


#------------------------------------------------- editar metas -------------------------------------------------
if menu == "Editar Metas":
    st.subheader("✏️ Editar Metas")
    data = st.text_input("Digite o período da meta que deseja editar (dd/mm - dd/mm): ").strip()
    if data:

        sucesso, metas = seleciona_metas(data)
        if not sucesso:
            st.error(metas)
            st.stop()

        st.subheader("📋 Metas encontradas:")
        for i, meta in enumerate(metas, start=1):
            st.write(f"✔️ Meta {i} - {meta.get('nome', 'Sem nome')} | {meta.get('tempo', 0)} minutos")

        with st.form("editar_metas"):
            indice = st.number_input("Número da meta que deseja editar:", min_value=1, max_value=len(metas)) - 1
            novo_nome = st.text_input("Novo nome: ").strip()
            novo_tempo = st.number_input("Novo tempo (minutos): ", min_value=1)

            enviar = st.form_submit_button("Confirmar")

            if enviar:
                sucesso, mensagem = editar_metas_por_indice(indice, data, novo_nome, novo_tempo)
                if sucesso:
                    st.success(mensagem)
                else:
                    st.error(mensagem)

#------------------------------------------------ excluir metas --------------------------------------------------
if menu == "Excluir Metas":
    st.subheader("🗑️ Excluir Metas")

    data = st.text_input("Digite a data da meta que deseja excluir (dd/mm - dd/mm: ").strip()

    if data:
        sucesso, metas = seleciona_metas(data)

        if not sucesso:
            st.error(metas)
            st.stop()

        st.subheader("Metas Encontradas:")
        for i, meta in enumerate(metas, start=1):
            st.write(f"✔️ Meta {i} - {meta.get('nome', 'Sem nome')} | {meta.get('tempo', 0)} minutos" )

        with st.form("excluir metas"):
            indice = st.number_input(f"Digite o número da meta que deseja excluir: ", min_value=1, max_value=len(metas)) - 1
            enviar = st.form_submit_button("Confirmar")

            if enviar:
                sucesso, mensagem = excluir_metas_por_indice(data, indice)
                if sucesso:
                    st.success(mensagem)
                else:
                    st.error(mensagem)
                    st.stop()

        with st.form("excluir_periodo"):
            st.subheader(f"Excluir semana - {data}")
            st.write("⚠️ Ao excluir o período, todas as metas presentes nele serão automaticamente excluídas.")
            enviar = st.form_submit_button("Confirmar")
            if enviar:
                sucesso, mensagem = excluir_metas_por_periodo(data)
                if sucesso:
                    st.success(mensagem)
                else:
                    st.error(mensagem)
                    st.stop()

#------------------------------------------------ ver relatório --------------------------------------------------
if menu == "Exibir Relatório":
    st.subheader("📊 Meu Relatório Semanal")

    periodo = st.text_input("Digite o período (dd/mm - dd/mm):")
    if st.button("Gerar Relatório"):
        resultado = gerar_relatorio(periodo)
        st.markdown(resultado.replace("\n", "  \n"))
