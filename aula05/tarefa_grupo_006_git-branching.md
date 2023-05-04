### Tarefa 006: Git Branching - 28/04/2023

1. Qual o nome do branch padrão do Git?
    - O nome do branch padrão do Git é master (ou main em algumas versões mais recentes).
2. O que o comando **<code>git branch nome</code>** realiza?
    - O comando git branch nome cria um novo branch com o nome especificado. Esse novo branch é criado a partir do commit atual (ou HEAD) e não altera o branch atual.
3. Como criar um branch a partir de um commit específico?
    - Para criar um branch a partir de um commit específico, é necessário fornecer o hash do commit como referência ao comando `git branch nome_do_branch hash_do_commit`. Por exemplo, se o hash do commit desejado for "abc123", o comando seria `git branch experimento abc123`.
4. Em um repositório, qual o efeito do comando **<code>git checkout -b bugfix/234</code>**?
    - O comando git checkout -b bugfix/234 cria um novo branch chamado "bugfix/234" a partir do branch atual (HEAD) e altera o branch atual para o novo branch criado.
5. Qual o comando para se alternar para um branch de nome **experimento2**?
    - O comando para se alternar para um branch de nome experimento2 é `git checkout experimento2`.
6. Em um repositório com dois branches, **b1** e **b2**, onde b1 é o corrente, qual o efeito do comando **<code>git branch</code>**?
    - O comando `git branch` lista todos os branches existentes no repositório. No caso descrito, seria listado os branches b1 e b2 e o branch atual seria destacado com um asterisco.
7. O que o comando **<code>git checkout -b</code>** nome faz?
    - O comando `git checkout -b` cria um novo branch com o nome especificado e altera o branch atual para o novo branch criado. Por exemplo, git checkout -b experimento cria um novo branch chamado "experimento" e altera o branch atual para o novo branch criado.
8. Qual a função do <code>**comando git branch -d teste</code>**?
    - O comando git branch -d teste exclui o branch com o nome "teste". Esse comando só pode ser executado se o branch a ser excluído não tiver commits que não foram mesclados (merged) em outro branch.
9. Durante o desenvolvimento de um software é comum, por exemplo, utilizar um novo recurso por meio de experimentação. Talvez uma nova tecnologia, uma nova biblioteca que pode ser útil ao que está em desenvolvimento, ou até mesmo uma nova versão de um produto já empregado. Para que o uso deste novo recurso não interfira com o que é considerado pronto, um branch pode ser criado para a experimentação. Código que for criado para a experimentação existirá apenas no branch criado. Se eventualmente o experimento demonstrar um resultado satisfatório, as alterações realizadas no branch poderão ser incorporadas no que é considerado pronto, ou seja, no branch principal (master). Esta última ação é conhecida por merge. Neste item, crie uma sequência de comandos que simula um caso simples de criação e uso seguido de merge empregando um branch para ilustrar uma experimentação conforme acima. A sequência deve incluir, obrigatoriamente: (a) criação de um ou mais branches; (b) chaveamento para pelo menos dois branches e (c) merge.
    - Suponha que você está no branch "master" e deseja criar um novo branch para experimentação chamado "experimento1":
    ```
    git branch experimento1   # cria o novo branch
    git checkout experimento1   # muda para o novo branch
    ```
    - Agora você pode fazer as alterações que desejar no código, adicionando arquivos, editando arquivos existentes, etc.
    - Suponha que você tenha feito algumas alterações no branch "experimento1" e queira mesclá-las no branch "master":
    ```
    git checkout master   # muda para o branch master
    git merge experimento1   # mescla as alterações do branch experimento1 no branch master
    ```
    - Se não houver conflitos entre as alterações nos dois branches, a mesclagem será concluída com sucesso. Se houver conflitos, o Git solicitará que você resolva os conflitos manualmente antes de concluir a mesclagem.