# StreamlitPython

**Projeto de Acompanhamento da Evolução dos Preços das Ações com Streamlit, Pandas e YFinance**

### Introdução
O mercado de ações é um ambiente dinâmico e volátil, onde a análise de dados desempenha um papel fundamental na tomada de decisões estratégicas. Para facilitar o acompanhamento da evolução dos preços das ações, foi desenvolvido um projeto utilizando **Streamlit**, **Pandas** e **YFinance**, permitindo a extração, visualização e análise interativa dos dados financeiros.

### Tecnologias Utilizadas
- **Streamlit**: Framework utilizado para criar uma interface web interativa de forma rápida e eficiente.
- **Pandas**: Biblioteca para manipulação e análise de dados, essencial para tratar os dados históricos das ações.
- **YFinance**: API utilizada para obter dados financeiros do Yahoo Finance de forma simples e automatizada.

### Funcionalidades do Projeto
1. **Seleção de Ativos**: O usuário pode inserir o código da ação desejada (por exemplo, PETR4.SA para ações da Petrobras) e definir um período para análise.
2. **Coleta de Dados**: O YFinance é utilizado para buscar os preços históricos da ação, incluindo valores de abertura, fechamento, mínima, máxima e volume de negociações.
3. **Visualização Gráfica**: Utilizando Pandas e bibliotecas de visualização como Matplotlib e Seaborn, os dados são exibidos em gráficos interativos, facilitando a interpretação das tendências de preços.
4. **Cálculo de Indicadores**: São calculadas métricas importantes como médias móveis, volatilidade e retorno acumulado, ajudando na avaliação do desempenho da ação.
5. **Interface Interativa**: Com o Streamlit, os usuários podem interagir com filtros e visualizar diferentes períodos de análise, tornando o acompanhamento dos ativos mais dinâmico e intuitivo.

### Importância da Análise de Ações
A análise da evolução dos preços das ações é essencial para investidores e analistas financeiros, pois:
- **Auxilia na Tomada de Decisão**: Permite identificar tendências e momentos oportunos para compra e venda de ativos.
- **Garante um Monitoramento Contínuo**: Com um sistema automatizado, os usuários podem acompanhar o mercado em tempo real.
- **Fornece Indicadores Estratégicos**: A análise de métricas como volatilidade e médias móveis contribui para uma melhor gestão de riscos.
- **Facilita a Compreensão Visual**: Gráficos interativos tornam a interpretação dos dados mais acessível e intuitiva.

### Conclusão
Este projeto demonstra como a combinação de **Streamlit, Pandas e YFinance** pode proporcionar uma ferramenta poderosa para acompanhamento do mercado financeiro. A automação na coleta de dados e a apresentação interativa tornam o processo de análise mais ágil e eficiente, auxiliando investidores e entusiastas do mercado de ações a tomarem decisões baseadas em dados concretos.
