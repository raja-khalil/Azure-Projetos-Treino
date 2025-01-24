# Criação de Máquina Virtual no Azure Usando Python

Este projeto demonstra como criar uma máquina virtual no Azure utilizando Python. Abaixo está o passo a passo para implementar esta funcionalidade de forma eficiente e escalável.

## Passo 1: Instalar as Bibliotecas Necessárias

1. Instale as bibliotecas `azure-mgmt-compute` e `azure-mgmt-resource`.

## Passo 2: Autenticação

1. Utilize as bibliotecas `azure.identity` e `azure.mgmt.resource` para configurar a autenticação.
2. Configure as credenciais usando `DefaultAzureCredential`.

## Passo 3: Configurar o Grupo de Recursos

1. Crie ou atualize um grupo de recursos especificando o nome do grupo e a localização.

## Passo 4: Configurar os Parâmetros da Máquina Virtual

1. Defina os parâmetros da máquina virtual, incluindo:
   - Perfil de hardware
   - Perfil de armazenamento
   - Perfil do sistema operacional
   - Perfil de rede

## Passo 5: Criar a Máquina Virtual

1. Inicie a criação da máquina virtual utilizando os parâmetros definidos anteriormente.
2. Aguarde a conclusão da criação da máquina virtual.

## Dicas Finais

- **Segurança**: Utilize senhas fortes e seguras.
- **Escalabilidade**: Escolha o tamanho da máquina virtual adequado às suas necessidades. Você pode alterar o tamanho posteriormente.
- **Manutenção**: Utilize tags para facilitar o gerenciamento de recursos.

---

Com esses passos, você conseguirá criar uma máquina virtual no Azure usando Python, de forma escalável e eficiente.
