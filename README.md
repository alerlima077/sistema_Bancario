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


O projeto foi **modularizado em funções**, seguindo boas práticas:

### 🔹 `depositar(saldo, valor, extrato, /)`
- **Argumentos por posição (positional only)**  
- Recebe o saldo, valor e extrato.  
- Atualiza saldo e extrato.  
- Retorna o saldo e extrato atualizados.  

---

### 🔹 `sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)`
- **Argumentos por nome (keyword only)**  
- Verifica regras de saque:  
  - saldo suficiente  
  - limite por saque  
  - limite de quantidade de saques  
- Atualiza saldo, extrato e contador de saques.  
- Retorna os valores atualizados.  

---

### 🔹 `exibir_extrato(saldo, /, *, extrato)`
- **Mistura de argumentos posicionais e nomeados**  
- Mostra todas as movimentações realizadas e o saldo disponível.  

---

### 🔹 `criar_usuario(usuarios)`
- Cria um usuário (cliente) do banco.  
- Campos: **nome, data de nascimento, CPF, endereço**.  
- O **CPF deve ser único** (não é permitido cadastrar dois usuários com o mesmo CPF).  

---

### 🔹 `criar_conta(agencia, numero_conta, usuarios)`
- Cria uma nova conta bancária vinculada a um usuário já cadastrado.  
- Estrutura da conta: **agência (fixa "0001"), número da conta (sequencial), usuário vinculado**.  
- O mesmo usuário pode ter várias contas.  

---

### 🔹 `listar_contas(contas)`
- Lista todas as contas criadas no sistema.  
- Exibe: **agência, número da conta e titular**.  

---

## 📂 Estrutura dos Dados

### Usuário e Conta
```python
{
  "nome": "João Silva",
  "data_nascimento": "01-01-1990",
  "cpf": "12345678900",
  "endereco": "Rua A, 100 - Bairro B - Cidade/UF"
}

{
  "agencia": "0001",
  "numero_conta": 1,
  "usuario": {dados do usuário}
}





