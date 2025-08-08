# 🌷 Habit's Garden 🌷

> *Cultivando a pessoa que você quer ser, uma semana de cada vez.*

## 📖 Sobre o Projeto

O **Habit's Garden** é uma aplicação de gerenciamento de hábitos e metas pessoais com foco no progresso semanal. Foi desenvolvida com o objetivo de tornar o acompanhamento de metas mais gerenciável e motivador, permitindo que novos hábitos sejam cultivados de forma mais consistente.

### 🎯 Motivação

Este projeto foi criado para me ajudar a:
- Estabelecer metas semanais realistas.
- Acompanhar o meu progresso de forma visual e mais motivadora.  
- Manter a minha consistência nos estudos, mas principalmente no autocuidado.
- Transformar os meus objetivos maiores em marcos semanais alcançáveis, reduzindo a ansiedade.

## ✨ Funcionalidades

### 📋 Gestão de Tarefas
- ✅ Adicionar, editar e excluir tarefas diárias.
- 🏷️ Categorização (estudo, autocuidado, trabalho, pessoal).
- ⏰ Controle de tempo gasto em minutos.
- 📝 Observações opcionais para cada tarefa.

### 🎯 Gestão de Metas
- ✅ Definir metas semanais para diferentes atividades.
- ⏰ Estabelecer tempo objetivo para cada meta.
- 📊 Acompanhar múltiplas metas por período.
- 🗑️ Gerenciar metas individualmente ou por período completo.

### 📊 Relatório semanal
- 📈 Relatório semanal com comparação meta vs. o que foi realizado.
- 💯 Cálculo de porcentagem de progresso.
- 📊 Barra de progresso visual na página inicial.
- 🎯 Mensagens motivacionais baseadas no desempenho.

### 💫 Extras
- 🌟 Frases motivacionais aleatórias na página principal.
- 🎨 Interface amigável com tema floral.
- 📱 Layout responsivo.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**.
- **Streamlit** - Interface web interativa.
- **JSON** - Persistência de dados local.
- **datetime** - Manipulação de datas.
- **random** - Seleção de frases motivacionais.

## 📁 Estrutura do Projeto

```
habits-garden/
│
├── app.py                # Aplicação principal Streamlit
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação
│
├── modulos/              # Módulos Python
│   ├── registro.py       # Gestão de tarefas
│   ├── metas.py          # Gestão de metas
│   ├── relatorios.py     # Geração de relatórios
│   ├── utilidades.py     # Funções auxiliares
│   └── quotes.txt        # Frases motivacionais
│
└── dados/                # Arquivos de dados (criados automaticamente)
    ├── tarefas.json      # Dados das tarefas
    └── metas.json        # Dados das metas
```

## 🚀 Como Usar

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```
git clone https://github.com/raytrin/habits-garden.git
cd habits-garden
```

2. Instale as dependências:
```
pip install -r requirements.txt
```

3. Execute a aplicação:
```
streamlit run app.py
```

4. Abra o navegador e acesse: `http://localhost:8501`

### Primeiros Passos

1. **Defina suas metas**: Vá até "Adicionar Metas" e estabeleça objetivos semanais.
2. **Registre tarefas**: Use "Adicionar Tarefas" para adicionar as suas atividades diárias.
3. **Acompanhe progresso**: Visualize o seu desempenho na "Página Inicial".
4. **Gere relatórios**: Use "Exibir Relatório" para análise semanal mais detalhada.

## 📊 Exemplo de Uso 

```
Meta Semanal: Python - 270 minutos
Tarefas Registradas: 
- 22/07: Python - 200min (estruturas de dados)
- 23/07: Python - 80min (POO)

Resultado: 280 minutos (103.7% da meta) ✅
```

## 🔄 Funcionalidades Futuras

- [ ] **Gráficos interativos** nos relatórios. 
- [ ] **Envio automático de relatórios** por email (via PythonAnywhere).
- [ ] **Sistema de login**.
- [ ] **Pesquisa e filtros** avançados por nome/categoria.
- [ ] **Dashboard analytics** com métricas históricas.

## 🧠 Aprendizados

Este projeto me permitiu aplicar conhecimentos em:
- **Estruturação de código** modular e reutilizável.
- **Manipulação de JSON** para persistência de dados.
- **Desenvolvimento web** com Streamlit.
- **Validação de dados** e tratamento de erros.
- **Design de interface** centrado no usuário.

---

*"The only thing worse than starting something and failing ... is not starting something." - Seth Godin 🌱"*