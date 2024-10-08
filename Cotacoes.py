import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta

# Criar as funções de carregamento de dados
# Cotações do Itaú - ITBU4 - 2010 a 2024


# Armazena os dados da funcao em cache
# Funcao criada para armazenar dados onde vai receber o nome da empresa
@st.cache_data
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)  # atributo da lib
    cotacoes_acao = dados_acao.history(
        period="1d", start="2018-01-01", end=None)  # atributo history da lib st
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao


@st.cache_data
def carregar_tickers_acoes():
    base_tickers = pd.read_csv("IBOV.csv", sep=";")
    tickers = list(base_tickers["Código"])
    tickers = [item + ".SA" for item in tickers]
    return tickers


acoes = carregar_tickers_acoes()
dados = carregar_dados(acoes)


# Cria a interface no Streamlit
st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações do Itaú (ITUB4) ao longo dos anos
""")  # markdown

# Prepara as visualizacoes e filtros
st.sidebar.header("Filtros")

# Filtros
lista_acoes = st.sidebar.multiselect("Escolha as ações: ", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})

# filtro de datas
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_data = st.sidebar.slider("Periodo: ",
                                   min_value=data_inicial,
                                   max_value=data_final,
                                   value=(data_inicial, data_final),
                                   step=timedelta(days=15))

dados = dados.loc[intervalo_data[0]:intervalo_data[1]]

# Criar grafico de linha
st.line_chart(dados)

texto_performance_ativos = ""

if len(lista_acoes) == 0:
    lista_acoes = list(dados.columns)
elif len(lista_acoes) == 1:
    dados = dados.rename(columns={"Close": acao_unica})

for acao in lista_acoes:
    perfomance_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
    perfomance_ativo = float(perfomance_ativo)
    if perfomance_ativo > 0:
        texto_performance_ativos = texto_performance_ativos + \
            f"  \n{acao}: :green[{perfomance_ativo:.1%}]"
    elif perfomance_ativo < 0:
        texto_performance_ativos = texto_performance_ativos + \
            f"  \n{acao}: :red[{perfomance_ativo:.1%}]"
    else:
        texto_performance_ativos = texto_performance_ativos + \
            f"  \n{acao}: {perfomance_ativo:.1%}"


st.write(f"""
#### Performance dos Ativos
Essa foi performance de cada ativos no período selecionado:
{texto_performance_ativos}
""")
