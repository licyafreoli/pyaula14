# Gerenciamento de Reservas - Refúgio dos Sonhos 🏨  

Este é um sistema simples para gerenciar reservas de quartos em um hotel. Ele permite que você adicione clientes, quartos, faça reservas e visualize as informações das reservas ativas e dos quartos disponíveis. O sistema foi implementado em Python utilizando a biblioteca [Flet](https://flet.dev/), que permite criar interfaces gráficas de maneira simples e eficiente.

## Funcionalidades

- **Adicionar clientes**: Registre clientes com nome, telefone e e-mail.
- **Adicionar quartos**: Adicione quartos com número, tipo (ex: Single, Double, Suite) e preço.
- **Verificar quartos disponíveis**: Consulte os quartos disponíveis para reserva.
- **Criar reservas**: Realize reservas associando um cliente a um quarto e informando as datas de check-in e check-out.
- **Cancelar reservas**: Permite cancelar uma reserva, tornando o quarto novamente disponível.
- **Exibir informações**: Mostra a lista de clientes, quartos e reservas.

## Tecnologias Usadas

- **Python 3.x**
- **Flet**: Biblioteca para criação de interfaces gráficas.
- **UUID**: Para gerar identificadores únicos para os clientes.

## Como Rodar

1. **Instalar as dependências**:
   
   Certifique-se de ter o Python 3.x instalado no seu ambiente. Em seguida, instale a biblioteca Flet:

   ```bash
   pip install flet
