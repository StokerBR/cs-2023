# Tarefa 021 - Teste de Software - 28/07/2023

**DEFINIÇÃO**:
1. Definir um conjunto de classes de Equivalência e um conjunto de casos de testes derivados, para testar a seguinte função de avaliação universitária. Por fim implementar este conjunto de casos de testes considerando a implementação deste programa constante do arquivo **avaliacaoEscolar.rar**, disponível no SIGAA.
2. A função avaliação, recebe como parâmetros os seguintes dados:
   2.1. **nota1** (numérico de ponto flutuante com duas casas decimais, sendo valores válidos de 0 a 10);
   2.2. **nota2**  (numérico de ponto flutuante com duas casas decimais);
   2.3. **cargaHoraria** (numérico inteiro, positivo);
   2.4. **faltas** (numérico inteiro, positivo).
3. Antes de efetuar qualquer cálculo, o sistema deverá validar os dados de entrada do usuário. Se algum destes valores for inválido, o sistema deve retornar a mensagem **Valores Inválidos**.
4. A forma de calcular a avaliação é a seguinte:

  4.1. Se a quantidade de faltas for superior a 25% da carga horária, o aluno estará reprovado por falta. Neste caso a função retorna a seguinte mensagem **Reprovado por Falta**;

  4.2. Estando o aluno reprovado por falta, não haverá a necessidade de se avaliar as notas;

  4.3. Se a média entre **nota1** e **nota2** for menor que 3.0, o aluno estará reprovado por média.  Neste caso a função retorna a seguinte mensagem **Reprovado por Média**;

  4.4. Se a média entre **nota1** e **nota2** for >= 3.0 e < 6.0, o aluno estará em recuperação.  Neste caso a função retorna a seguinte mensagem **Recuperação**;

  4.5 Em qualquer outra situação o aluno estará  aprovado. Então a função retornará a mensagem: **Aprovado**.
5. O Conjunto de classes de Equivalência deverá ser definido seguindo o seguinte padrão:

|id|descrição|V/I|
|--|--|--|
|CE01|nota1 < 0|I|

Onde:

**CE** = Classe de Equivalência, seguido de um número sequencial;

**Descrição** = define um cenário de teste;

**V/I** = Válida ou Inválida.

5. O Conjunto de casos de testes derivado das classes de Equivalência deve seguir o seguinte padrão:

|CT|Nota1|Nota2|CargaHoraria|Faltas|Resultado Esperado|Classe Equivalência|
|--|--|--|--|--|--|--|
|CT01|-2.00|8.00|128|12|Valor Inválido|CE1|

Onde:

**CT** = Caso de Teste, seguido de um valor sequencial;

**Nota1** é o valor informado para a variável nota1;

**Nota2** é o valor informado para a variável nota2;

**CargaHoraria** é o valor informado para a variável cargaHoraria;

**Faltas** é o valor informado para a variável faltas.

**Resultado esperado** é o resultado que se espera da execução da função;

**Classe de Equivalência** é a identificação de qual classe de equivalência está sendo exercitada pelo caso de teste.

**INSTRUÇÕES**

1. a Definição das classes de equivalência e os casos de testes devem constar deste arquivo. Vocês devem editá-lo para adicionar estes dados.
2. A implementação deve seguir o modelo implementado no arquivo informado no item 1. Se você implementar na Linguagem de Programação Java, basta entregar somente a classe de teste. Se implementar em outra linguagem, deve entregar a classe de implementação da funcionalidade e a classe de teste.
3. A entrega referente a esta tarefa deverá ser efetuada no seu repositório pessoal utilizado para a manutenção do controle de versão dos artefatos relacionados às tarefas da disciplina. Deve-se criar uma pasta chamada **tarefa021**, onde os arquivos devem ser disponibilizados.
4. O prazo para a conclusão desta tarefa é o dia 30/07/2023, as 23h59min.
