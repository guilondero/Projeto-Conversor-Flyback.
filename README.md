# ⚡️ Calculadora para Projeto de Conversor Flyback de Alta Tensão ⚡️

Este repositório contém um script em Python para o dimensionamento e cálculo dos componentes essenciais de um **conversor DC-DC Flyback de alta tensão**. O projeto foi desenvolvido como parte da disciplina de Eletrônica de Potência do curso de Engenharia de Controle e Automação da UFSM, com o objetivo de projetar um conversor robusto para aplicações de alta tensão a partir de uma entrada retificada da rede elétrica.

## 🎯 Objetivo do Projeto

O script calcula os parâmetros críticos para a construção de um conversor Flyback com base nas seguintes especificações de projeto:

| Parâmetro | Valor | Descrição |
| :--- | :--- | :--- |
| 🔌 **Tensão de Entrada (Pico)** | `311 V` | (220V RMS) |
| ⚡️ **Tensão de Saída** | `6000 V` | |
| 💡 **Potência de Saída** | `80 W` | |
| 🔄 **Frequência de Chaveamento** | `1.8 kHz` | |
| 🕒 **Razão Cíclica (Duty Cycle)** | `0.7` | |
| 🌊 **Ondulação de Corrente (Indutor)** | `15%` | |
| 🌊 **Ondulação de Tensão (Capacitor)** | `2%` | |

## 🛠️ O que o script calcula?

O arquivo `Projeto_Conversor.py` realiza os seguintes cálculos fundamentais para o projeto:

- **`n`**: Relação de transformação do transformador Flyback.
- **`Lm`**: Indutância de magnetização necessária para o primário.
- **`C`**: Capacitância do filtro de saída.
- **`Ro`**: Resistência de carga equivalente.
- **`IL`**: Corrente média no indutor.
- **`Vdss`**: Tensão máxima de bloqueio para o MOSFET.
- **`Vdmax`**: Tensão reversa máxima no diodo de saída.
- E outras correntes e tensões importantes para a seleção dos componentes.

## 🚀 Como usar

1.  **Clone o repositório e entre na pasta:**
    ```bash
    git clone https://github.com/seu-usuario/Projeto-Conversor-Flyback.git
    cd Projeto-Conversor-Flyback
    ```

2.  **Execute o script Python:**
    ```bash
    python Projeto_Conversor.py
    ```

3.  **Visualize os resultados:** Os valores calculados para os componentes e os parâmetros de operação serão impressos diretamente no seu terminal.

---

Este projeto demonstra a aplicação prática de conceitos de eletrônica de potência para resolver um desafio de engenharia real. Sinta-se à vontade para usar este código como referência para seus próprios projetos e estudos!
