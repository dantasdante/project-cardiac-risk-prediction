# Notebooks do Projeto

Os notebooks foram organizados em etapas seguindo a progressão lógica da organização do projeto, sendo cada notebook (`S1`, `S2`, `S3`, `S4`, `S5`) representando um STEP da modelagem.

## Sumário do Projeto

A seguir, apresentamos um breve sumário de cada etapa do projeto, que pode ser encontrada nos respectivos notebooks:

* **S1 - Análise Exploratória da Doença Cardíaca (`S1_analise_exploratoria_doencas_cardiacas.ipynb`)**:
    * Esta etapa inicial foca na compreensão aprofundada dos dados. Inclui a análise descritiva das variáveis, visualizações para identificar padrões e relacionamentos, e a detecção de insights preliminares sobre os fatores associados à doença cardíaca. É a fundação para todas as etapas subsequentes, garantindo que entendemos a natureza do nosso dataset.

* **S2 - Pré-processamento e Limpeza dos Dados (`S2_Preprocessing_Cleaning_doencas_cardiacas.ipynb`)**:
    * Nesta fase, o foco principal é a preparação dos dados brutos para a modelagem. Isso envolve a identificação e tratamento de valores ausentes, a correção de inconsistências, a remoção de duplicatas e outras operações de limpeza que garantem a qualidade e integridade do dataset.

* **S3 - Pré-processamento, Transformação e Modelagem (`S3_updated_preprocessing_Transformation_doencas_cardiacas.ipynb`)**:
    * A etapa S3 aprofunda o pré-processamento com a aplicação de transformações necessárias para otimizar os dados para algoritmos de Machine Learning. Isso pode incluir a normalização ou padronização de features, a codificação de variáveis categóricas (como One-Hot Encoding), e a engenharia de novas características. Além disso, nesta fase, é realizada a primeira modelagem do modelo matemático, como a Regressão Logística, definindo sua arquitetura inicial.

* **S4 - Otimização dos Parâmetros do Modelo (`S4_Otimizacao_SVM_Modelo_doencas_cardiacas.ipynb`)**:
    * Com um modelo base estabelecido, a etapa S4 se dedica à otimização de seus hiperparâmetros. Utilizando técnicas como Grid Search e validação cruzada, buscamos encontrar a melhor combinação de parâmetros que maximize o desempenho do modelo, garantindo sua robustez e capacidade de generalização para dados não vistos.

* **S5 - Explicabilidade e Interpretabilidade do Modelo (`S5_Explicabilidade_Modelo_doencas_cardiacas.ipynb`)**:
    * A fase final do projeto concentra-se em entender como o modelo toma suas decisões. Utilizando ferramentas como SHAP (SHapley Additive exPlanations), analisamos a contribuição de cada feature para as previsões do modelo, tanto em nível global (quais features são mais importantes no geral) quanto em nível local (como uma feature específica impacta uma previsão individual). Isso aumenta a confiança no modelo e permite extrair insights valiosos sobre os fatores de risco da doença cardíaca.

## Estrutura dos Notebooks

Cada notebook (`S1`, `S2`, `S3`, `S4`, `S5`) representa uma etapa sequencial do processo de modelagem, garantindo uma progressão lógica e organizada das fases do projeto.

---

### Como Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [Link do seu Repositório GitHub]
    ```
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd [Nome do seu Projeto]
    ```
3.  **Instale as dependências (se você tiver um `requirements.txt`):**
    ```bash
    pip install -r requirements.txt
    ```
    (Se não tiver, liste as principais bibliotecas como `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `plotly`, `shap`).
4.  **Abra os notebooks Jupyter:**
    ```bash
    jupyter notebook
    ```
    Você pode navegar até a pasta `notebooks/` e abrir cada arquivo `S<n>_*.ipynb` em sequência.

---

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar problemas, sinta-se à vontade para abrir uma issue ou enviar um pull request.
