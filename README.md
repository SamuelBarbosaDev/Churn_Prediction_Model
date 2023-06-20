# Churn_Prediction_Model:
### Índice

- [Churn\_Prediction\_Model:](#churn_prediction_model)
    - [Índice](#índice)
    - [Contextualização:](#contextualização)
    - [Metodologia Aplicada:](#metodologia-aplicada)
  - [Entendimento do Negócio:](#entendimento-do-negócio)
  - [Entendimento dos Dados:](#entendimento-dos-dados)
    - [Variáveis:](#variáveis)
    - [Verificando Valores Nulos:](#verificando-valores-nulos)
    - [Verificando Tipos:](#verificando-tipos)
  - [Preparação dos Dados:](#preparação-dos-dados)
  - [Modelagem:](#modelagem)
  - [Avaliação:](#avaliação)
  - [Implantação:](#implantação)
  - [Pré-requisitos para executar o projeto:](#pré-requisitos-para-executar-o-projeto)
    - [Instale o Pacote Anaconda:](#instale-o-pacote-anaconda)
    - [Ambiente virtual e Dependências:](#ambiente-virtual-e-dependências)


### Contextualização:
Você trabalha em uma plataforma de streaming e a diretoria está preocupada com o
alto índice de usuários cancelando as suas assinaturas. Eles acreditam que é possível
prever se um usuário tem mais chance de deixar a plataforma antes que isso aconteça,
e com base nessa informação tomar ações para reduzir o churn.
Seu objetivo é criar um modelo de classificação capaz de prever se um usuário tem
mais chance de cancelar a sua assinatura na plataforma ou não. Para isso, a empresa
forneceu uma base de dados em csv contendo dados sobre as contas dos clientes.

### Metodologia Aplicada:
A análise foi realizada utilizando o modelo CRISP-DM, o CRISP-DM (Cross Industry Standard Process for Data Mining) é um modelo padrão de processo para projetos de mineração de dados que define um conjunto de fases e tarefas que devem ser executadas para desenvolver soluções de mineração de dados efetivas.

![CRISP-DM](/core/img/CRISP-DM.png)

O modelo CRISP-DM é uma abordagem sistemática e estruturada para a mineração de dados que ajuda as empresas a desenvolver soluções de mineração de dados de maneira eficiente e eficaz, reduzindo o tempo e os custos do projeto.

## Entendimento do Negócio:

## Entendimento dos Dados:
### Variáveis:
![Data Frame](/core/img/dataframe.png)

### Verificando Valores Nulos:
![Data Frame](/core/img/nulos.png)

### Verificando Tipos:
![Data Frame](/core/img/tipos.png)

## Preparação dos Dados:

## Modelagem:

## Avaliação:

## Implantação:
Iniciando a etapa de implementação do modelo em produção.

## Pré-requisitos para executar o projeto:
Abaixo, listarei os requisitos necessários para que o projeto funcione corretamente.

### Instale o Pacote Anaconda:
Você pode baixá-lo em: <https://www.anaconda.com/download/> 

### Ambiente virtual e Dependências:
Criando ambiente virtual:
```
conda create -n .churn python=3.10.6
```

Entrando no ambiente virtual:
```
conda activate .churn
```

Instale as dependências:
```
pip install -r core/requirements.txt
```

---
Linkedin: <https://www.linkedin.com/in/samuel-barbosa-dev/> 

E-mail: <samueloficial@protonmail.com>