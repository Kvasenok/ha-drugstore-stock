# Drugstore Stock

Gerencie o estoque de remédios da sua casa no Home Assistant!

## Visão Geral

A integração do Drugstore Stock permite que você registre e monitore seu estoque de medicamentos no Home Assistant, ajudando você a controlar as quantidades disponíveis e identificar quando é hora de reabastecer.

## Instalação

### Método 1: Instalação via HACS  (Recomendado)

1. Certifique-se de ter o [HACS](https://hacs.xyz/) instalado em sua instância Home Assistant.
1. Vá em **HACS > 3 pontos > Custom repositories**
2. Adicione essa URL do repositório: `https://github.com/BigPiloto/ha-drugstore-stock`
3. Selecione a categoria (Type): `Integration`
4. Clique em `ADD`
5. Encontre e clique em `Drugstore Stock` na lista de integrações;
6. Clique em Download e instale;
7. Reinicie o Home Assistant.

### Método 2: Instalação manual

1. Baixe este repositório;
2. Copie a pasta `custom_components/drugstore_stock` para o diretório `custom_components/` do seu Home Assistant;
3. Reinicie o Home Assistant.

## Configuração

1. Acesse **Configurações > Dispositivos e Serviços > Adicionar Integração > procure por `Drugstore Stock`**;
2. De um nome para sua lista;
  2.1 (Opcional) Escolher uma Área (cadastrada no HA);
4. Clique em `Enviar`.

## Prints e Exemplos

> Adicione aqui imagens/gifs mostrando o funcionamento da integração!

## Suporte e Bugs

- Relate problemas ou sugestões em: [Issues](https://github.com/BigPiloto/ha-drugstore-stock/issues)

## Licença

[MIT License](LICENSE)
