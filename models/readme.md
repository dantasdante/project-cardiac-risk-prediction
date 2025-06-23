# Repositório do Modelo de Regressão Logística

Este repositório documenta o desenvolvimento e avaliação do modelo de Regressão Logística usado no projeto de previsão de risco de doença cardíaca. 
---

## Desempenho do Modelo de Regressão Logística

O modelo de Regressão Logística foi cuidadosamente otimizado e avaliado para garantir sua eficácia na previsão de risco de doença cardíaca. Abaixo, são apresentados os resultados de teste e validação cruzada, bem como a análise detalhada da matriz de confusão.

### Métricas de Teste

Após a otimização de hiperparâmetros (realizada na etapa S4), o melhor modelo de Regressão Logística foi avaliado no conjunto de dados de teste (dados não vistos durante o treinamento e otimização). As métricas alcançadas foram:

* **Recall (Revocação):** 0.93
* **Precision (Precisão):** 0.86
* **F1-Score:** 0.89
* **Average Precision (AP) na Curva Precision-Recall:** 0.91

Estes resultados indicam que o modelo é altamente eficaz em identificar casos positivos (Recall de 0.93), enquanto mantém uma boa precisão nas suas previsões (Precision de 0.86).

### Validação Cruzada

Para avaliar a robustez e a capacidade de generalização do modelo, foi realizada uma validação cruzada (KFold com 5 splits). As métricas médias obtidas na validação cruzada foram:

* **Recall Médio:** Aproximadamente 0.92
* **Precision Média:** Aproximadamente 0.86
* **Average Precision (AP) Média:** Aproximadamente 0.92

A consistência entre as métricas de teste e validação cruzada sugere que o modelo não está sofrendo de overfitting e generaliza bem para novos dados.

### Matriz de Confusão

A matriz de confusão normalizada por linha (`True label`) fornece uma visão detalhada do desempenho do modelo, mostrando as proporções de acertos e erros para cada classe.

### Matriz de Confusão Normalizada

|           | Previsão: Não Doença (0) | Previsão: Doença (1) |
| :-------- | :----------------------- | :------------------- |
| **Real: Não Doença (0)** | 0.81                     | 0.19                 |
| **Real: Doença (1)** | 0.065                    | 0.93                 |


### Curva Precision-Recall

A curva Precision-Recall ilustra o trade-off entre Precisão e Recall em diferentes limiares de classificação. Uma alta Área Sob a Curva (Average Precision = 0.91) indica um excelente desempenho do modelo, especialmente em classes desbalanceadas.


---

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar problemas, sinta-se à vontade para abrir uma issue ou enviar um pull request.
