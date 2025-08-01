![hacs custom](https://img.shields.io/badge/hacs-custom-orange.svg)
![HACS Default](https://img.shields.io/badge/HACS-Default-blue.svg)
![HACS Action](https://github.com/BigPiloto/ha-drugstore-stock/actions/workflows/validate.yaml/badge.svg)
![Validate with hassfest](https://github.com/BigPiloto/ha-drugstore-stock/actions/workflows/hassfest.yaml/badge.svg)
![Release](https://img.shields.io/github/v/release/BigPiloto/ha-drugstore-stock.svg)
![Downloads](https://img.shields.io/github/downloads/BigPiloto/ha-drugstore-stock/total.svg)
![Last commit](https://img.shields.io/github/last-commit/BigPiloto/ha-drugstore-stock.svg)

# Drugstore Stock

Gerencie o estoque de remédios da sua casa no Home Assistant!

Drugstore Stock é uma integração (custom component) para o Home Assistant. Ela funciona no back-end, processando e expondo os dados das listas de estoque como entidades no Home Assistant.

Para visualizar os dados do Drugstore Stock diretamente no painel (Lovelace), recomenda-se instalar também o cartão personalizado [Drugstore Stock Card](https://github.com/BigPiloto/ha-drugstore-stock-card). Esse cartão facilita a visualização e o gerenciamento das listas de estoque pela interface do Home Assistant.

## Visão Geral

A integração do Drugstore Stock permite que você registre e monitore seu estoque de medicamentos no Home Assistant, ajudando você a controlar as quantidades disponíveis e identificar quando é hora de reabastecer.

## Instalação

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=BigPiloto&repository=ha-drugstore-stock&category=Integration)

### Método 1: Instalação via HACS  (Recomendado)

1. Certifique-se de ter o [HACS](https://hacs.xyz/) instalado em sua instância Home Assistant
1. Vá em **`HACS` > `3 pontos` > `Custom repositories`**
2. Adicione essa URL do repositório: `https://github.com/BigPiloto/ha-drugstore-stock`
3. Selecione a categoria (Type): **`Integration`**
4. Clique em **`ADD`**
5. Encontre e clique em `Drugstore Stock` na lista de integrações
6. Clique em **`Download`** e instale
7. Reinicie o Home Assistant.

### Método 2: Instalação manual

1. Baixe este repositório
2. Copie a pasta `custom_components/drugstore_stock` para o diretório `custom_components/` do seu Home Assistant
3. Reinicie o Home Assistant

## Configuração

1. Acesse **`Configurações` > `Dispositivos e Serviços` > `Adicionar Integração` > procure por `Drugstore Stock`**;
2. De um nome para sua lista - (Opcional) Escolher uma Área (cadastrada no HA);
3. Clique em **`Enviar` > `Terminar`**;
4. Clique em **`Configurar`**
5. Selecione se quer **Adicionar, Editar ou Remover um medicamento**
6. Siga as instruções do card preenchendo as colunas

## Prints e Exemplos

> [Exemplos](../examples.pt-BR.md)

## Suporte e Bugs

- Relate problemas ou sugestões em: [Issues](https://github.com/BigPiloto/ha-drugstore-stock/issues)

## Licença

Este projeto está licenciado sob a licença do MIT - consulte o arquivo [MIT License](LICENSE) para obter detalhes.
