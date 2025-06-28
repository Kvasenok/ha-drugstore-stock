# Adicionando nova lista 📋

1. Vá na Integração `Drugstore Stock`
2. Clique em **`Adicionar Entrada`**
3. Coloque um nome para a lista (obrigatório) e selecione uma área (opcional)
4. Clique em **`Enviar` > `Terminar`**

<br>

# Adicionando novo medicamento 💊

1. Vá na Integração `Drugstore Stock`
2. Clique em **`Configurar`** na lista desejada
3. Selecione **`Adicionar novo medicamento` > `Enviar`**
4. Preencha as informações:
    - Nome do medicamento
    - Quantidade Inicial
    - Quantidade Mínima
    - Quantidade Máxima
    - Unidade de medida
5. Clique em **`Enviar` > `Terminar`**

<br>

# Editando medicamento existente 🩹💊

1. Vá na Integração `Drugstore Stock`
2. Clique em **`Configurar`** na lista desejada
3. Selecione **`Editar medicamento existente` > `Enviar`**
4. Selecione o **medicamento que quer alterar > `Enviar`**
5. Preencha as informações:
    - Nome do medicamento
    - Quantidade Inicial
    - Quantidade Mínima
    - Quantidade Máxima
    - Unidade de medida
6. Clique em **`Enviar` > `Terminar`**

<br>

# Removendo medicamento existente ❌

1. Vá na Integração `Drugstore Stock`
2. Clique em **`Configurar`** na lista desejada
3. Selecione **`Remover medicamento existente` > `Enviar`**
4. Selecione o **medicamento que quer remover > `Enviar`**
5. Selecione **`Confirmar remoção` > `Enviar` > `Terminar`**

Observação: Por segurança o Home Assistant não permite deletar uma entidade órfã automaticamente, pois no futuro se ela retornar ainda terá seu histórico, caso tenha certeza que queira deletar a entidade, prossiga da seguinte forma:

## Removendo entidade órfã de medicamento removido

1. Após remover o medicamento pela instrução anterior, clique em **`entidade`** e procure pela entidade removida
2. Clique em **`Configurações` > `Excluir` > `Excluir`**
