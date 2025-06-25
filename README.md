# Modelo de machine learning para predição do risco de doença arterial coronariana

[![Licença](https://img.shields.io/badge/Licença-MIT-blue.svg)](LICENSE)
> Um modelo preditivo para detecção precoce de risco de Doença Arterial Coronariana, visando a prevenção e a redução de custos na saúde.
> As doenças cardiovasculares (DCVs) são a principal causa de mortalidade global, com impactos sociais e econômicos devastadores. No Brasil, os custos diretos e indiretos associados a condições como a insuficiência cardíaca são bilionários anualmente, e projeções internacionais apontam para um crescimento exponencial.

Este projeto propõe o desenvolvimento de um **modelo preditivo, usando aprendizagem supervisionada** para **estimar a probabilidade de um indivíduos desenvolver Doença Arterial Coronariana (DAC)**. Nossa abordagem busca democratizar o acesso a diagnósticos preventivos, reduzir custos hospitalares e mitigar o impacto econômico dessas patologias, posicionando a prevenção como um pilar fundamental na saúde pública por meio de um aplicativo - **PrevenCor**.

[![Faça o teste clicando aqui](https://img.shields.io/badge/Faça%20o%20teste%20clicando%20aqui-8A2BE2)](https://project-cardiac-risk-prediction-prevencor.streamlit.app/)

---

## 🧐 O Problema

As Doenças Cardiovasculares (DCVs) representam a principal causa de mortalidade e morbidade global. Elas não apenas impactam severamente a qualidade de vida, mas também geram custos significativos para os sistemas de saúde. No Brasil, a insuficiência cardíaca (IC) impõe um ônus financeiro de R$ 6 bilhões anuais em produtividade perdida e R$ 38,2 milhões em custos diretos ao SUS somente em 2024. Projeções internacionais, como as dos Estados Unidos, indicam que o custo da IC pode aumentar em 124% até 2050 (de US$ 260 bilhões para US$ 584 bilhões), enquanto na Europa, as DCVs custaram à economia da União Europeia € 282 bilhões em 2021.

Diante desse cenário, reconhece-se que 90% dos casos poderiam ser prevenidos com detecção precoce e controle dos fatores de risco.

## 💡 A Solução Proposta

Para enfrentar esse desafio, este projeto propõe o desenvolvimento de um **modelo de Machine Learning** capaz de identificar, de forma precoce, indivíduos com maior propensão a desenvolver doenças cardiovasculares a partir do resultado de exames.

Nossa abordagem visa:
* **Democratizar o acesso a diagnósticos precoces**: Tornando a detecção de risco mais acessível.
* **Reduzir custos hospitalares**: Evitando tratamentos caros e invasivos em estágios avançados da doença.
* **Mitigar o impacto econômico**: Promovendo a prevenção como um pilar fundamental na saúde pública.

* ## 📊 Dados Utilizados

O modelo foi desenvolvido utilizando um **dataset anonimizado**, composto por **917 registros de pacientes** de hospitais da Hungria, Suíça e Estados Unidos. A fonte do dataset é a **UC Irvine (University of California, Irvine)**, uma base de dados amplamente reconhecida na comunidade de Machine Learning.

Foram analisadas **13 características clínicas relevantes** para a predição da Doença Arterial Coronariana (DAC).

## 🧠 Metodologia e Desempenho do Modelo

Nosso projeto utiliza um **modelo de Machine Learning supervisionado**. Após o treinamento e avaliação, o algoritmo demonstrou alta capacidade preditiva, alcançando:

* **Sensibilidade (Recall): 92%** para o diagnóstico de casos verdadeiros.

A escolha do **recall como métrica primária** é estratégica, pois nosso objetivo é **minimizar o número de falsos negativos**, garantindo que o máximo de pacientes em risco seja identificado. Essa abordagem é crucial para ações preventivas e para evitar desfechos graves e custos elevados de tratamento em estágios avançados da doença.

## 💰 Impacto Econômico Potencial

Alcançando o sucesso (evitando a doença com a prevenção) ao menos 50% do público que sofre com doença cardíacas é possível estimar uma economia em cerca de R$700 milhões por ano, e algo em torno de 92 mil vidas salvas. Essa projeção baseia-se na premissa de que a detecção precoce e a prevenção poderiam impactar positivamente até 50% dos casos, reduzindo significativamente os custos associados ao tratamento de estágios avançados da doença.

[![Sumário Executivo](https://img.shields.io/badge/Para%20sum%C3%A1rio%20executivo%20clique%20aqui-FFFF00)](https://github.com/dantasdante/project-cardiac-risk-prediction/blob/main/relatorios/Summary%20Executive.pdf))

---

## ⚠️ Aviso Importante

É fundamental ressaltar que este modelo é uma **ferramenta de apoio**, desenvolvida para **fins didáticos e demonstrativos**. Ele **NÃO substitui o diagnóstico médico profissional** e deve ser complementado por outras variáveis clínicas e exames. Seu uso deve ser sempre sob supervisão e interpretação de especialistas da saúde. **A decisão final sobre o diagnóstico e tratamento pertence sempre aos profissionais de saúde.**

---

## 🚀 Como Usar/Executar

Para executar o projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-seu-repositorio.git](https://github.com/seu-usuario/nome-do-seu-repositorio.git)
    cd nome-do-seu-repositorio
    ```
2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: `venv\Scripts\activate`
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    (Certifique-se de ter um arquivo `requirements.txt` com todas as bibliotecas necessárias)

4.  **Execute o aplicativo Streamlit:**
    ```bash
    streamlit run app.py  # Ou o nome do seu arquivo principal do Streamlit
    ```
    O aplicativo será aberto no seu navegador padrão.

    ## 📂 Estrutura do Projeto

* `data/`: Contém o dataset utilizado (`heart_disease_uci.csv` ou similar).
* `notebooks/`: Jupyter notebooks com a exploração de dados, pré-processamento e treinamento do modelo.
* `src/`: Scripts Python com funções auxiliares e o código do modelo.
* `app.py`: Arquivo principal do aplicativo Streamlit.
* `models/`: Modelos treinados salvos (ex: `.pkl` ou `.joblib`).
* `requirements.txt`: Lista de dependências do Python.
* `LICENSE`: Arquivo de licença do projeto.
* `README.md`: Este arquivo.

* ## 🛠️ Tecnologias Utilizadas

* Python
* Pandas (para manipulação de dados)
* NumPy (para operações numéricas)
* Scikit-learn (para construção e avaliação do modelo de ML)
* Streamlit (para interface do usuário)
* Matplotlib/Seaborn (para visualização de dados)

* ## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum problema, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📧 Contato

Se você tiver alguma dúvida, sugestão ou colaboração, entre em contato:

* **Nome:** Dante Dantas
* **LinkedIn:** linkedin.com/in/dante-dantas
