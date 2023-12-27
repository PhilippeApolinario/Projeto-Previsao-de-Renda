# Previsão de Renda por meio de Árvore de Regressão

### 1. Entendimento do Problema
Uma instituição financeira enfrenta o desafio de aprimorar a avaliação do perfil de renda de seus novos clientes, visando otimizar a definição dos limites de cartões de crédito. A necessidade de uma abordagem mais precisa na determinação dos limites é imporntate para proporcionar uma experiência personalizada aos clientes, ao mesmo tempo em que fortalece a gestão de riscos da instituição.

### 2. Premissas do Negócio
* A renda dos clientes é uma métrica fundamental para a definição de limites de cartões de crédito.
* As variáveis disponíveis no conjunto de dados são relevantes para estimar a renda dos clientes.

### 3. Estratégia Utilizada
Na fase de análise descritiva, foram explorados os dados disponíveis para compreender e organizar o perfil de renda dos clientes. Posteriormente, a modelagem foi realizada utilizando o DecisionTreeRegressor, uma técnica de Machine Learning. A árvore de regressão resultante foi interpretada para extrair insights sobre as variáveis mais impactantes no perfil de renda dos clientes. Esta estratégia visa otimizar a definição dos limites de cartões de crédito, proporcionando uma melhor experiência para os clientes e fortalecendo a gestão de riscos da instituição. Além disso, foi criado um webapp para disponibilizar essa análise.

### 4. Principais Insights Obtidos

* 60,9% não possuem veículo.
* 67,6% possuem imóvel.
* 69,2% não possuem filhos.
* Podemos observar que o índice de clientes que possuem veículo aumenta conforme a renda também aumenta.
* Em relação a posse de imóvel já não ocorre tanta alteração.
* A árvore de regressão destacou as variáveis mais relevantes na estimativa de renda dos clientes, oferecendo insights sobre fatores como histórico de crédito, histórico de transações e idade.


### 5. Produto Final
O produto final consiste em um modelo treinado utilizando o DecisionTreeRegressor, capaz de prever a renda dos clientes com base em diferentes variáveis explicativas. Além disso, o projeto oferece uma análise descritiva dos dados e insights sobre o perfil de renda dos clientes disponibilizados através de um webapp.

### 6. Conclusão
A implementação desta solução proporciona uma abordagem mais precisa na determinação de limites de cartões de crédito, melhorando a experiência do cliente e fortalecendo a gestão de riscos da instituição financeira. A combinação de análise descritiva e modelagem com DecisionTreeRegressor oferece uma visão aprofundada do perfil de renda dos clientes, permitindo uma tomada de decisão mais informada e eficaz.

## Utilização

### Dependências

* Sistema Operacional:
    * Windows 10 ou 11

* Bibliotecas e Módulos:
    * Numpy 
    * Pandas
    * Matplotlib
    * Seaborn
    * Pandas Profiling
    * Scikit-learn
    * Streamlit 

## Autores

Nomes dos desenvolvedores do projeto e informação para entrar em contato.

 Philippe Apolinário  
 [@PhilippeApolinario](https://www.linkedin.com/in/philipperapolinario/)

## Histórico de versões.

* 0.1
    * Primeira versão

## Licença de uso

Esse projeto possui licença de uso [MIT] - acesse o arquivo LICENSE.md para mais detalhes.
