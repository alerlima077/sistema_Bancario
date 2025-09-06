# 💰 Sistema Bancário em Python

Este projeto foi desenvolvido como parte do **Vivo - Python AI Backend Developer da DIO**.  
O objetivo é simular um **sistema bancário simples**, permitindo operações de **depósito, saque, extrato e saída**.

---

## 📝 Funcionalidades

O sistema implementa as seguintes operações:

- **Depósito**  
  - Permite adicionar valores à conta.  
  - Valores negativos ou iguais a zero são rejeitados.  

- **Saque**  
  - Permite realizar saques, respeitando as seguintes regras:  
    - Valor máximo por saque: **R$ 500,00**  
    - Máximo de **3 saques por dia**  
    - Não permite saque com valor negativo ou maior que o saldo disponível  

- **Extrato**  
  - Mostra o histórico de movimentações (depósitos e saques)  
  - Mostra o **saldo final**  

- **Sair**  
  - Encerra o sistema.  

---

## 🖥️ Menu de Operações

Ao executar o programa, o usuário visualiza o seguinte menu:

======-NOSSO BANCO S.A-======

[1] Depositar  
[2] Sacar  
[3] Extrato  
[0] Sair  



---

## 📂 Estrutura do Código

- Variáveis principais:
  - `saldo`: armazena o valor atual da conta  
  - `limite`: define o valor máximo de saque por operação  
  - `extrato`: guarda o histórico de operações  
  - `numero_saque`: contador de saques realizados  
  - `LIMITE_SAQUES`: constante que define o limite diário de saques  

- Estrutura de repetição:  
  - O programa usa um `while True` para exibir o menu continuamente até que o usuário escolha sair.  

- Estrutura condicional:  
  - Cada operação (`depositar`, `sacar`, `extrato`, `sair`) é controlada por condicionais `if / elif / else`.  

---

## 🚀 Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/alerlima077/sistema_Bancario.git

cd sistema_Bancario

python sistema_bancario.py

======-NOSSO BANCO S.A-======

[1] Depositar  
[2] Sacar  
[3] Extrato  
[0] Sair  

=> 1  
Informe o valor do depósito: 200

=> 2  
Informe o valor do saque: 50

=> 3    

===============EXTRATO==============  

Depósito: R$ 200.00   

Saque: R$ 50.00   

Saldo: R$ 150.00    

====================================

