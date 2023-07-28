# Resposta tarefa 021

## Classes de Equivalência

| Classe Equivalência | Descrição                                                                             |
| ------------------- | ------------------------------------------------------------------------------------- |
| CE01                | Nota1 menor que 0                                                                     |
| CE02                | Nota1 maior que 10                                                                    |
| CE03                | Nota2 menor que 0                                                                     |
| CE04                | Nota2 maior que 10                                                                    |
| CE05                | Faltas menor que 0                                                                    |
| CE06                | Faltas maior que cargaHoraria                                                         |
| CE07                | CargaHoraria menor que 0                                                              |
| CE08                | Média maior ou igual a 7 e faltas menor ou igual a 25% da carga horária               |
| CE09                | Faltas maior que 25% da carga horária                                                 |
| CE10                | Média menor que 3                                                                     |
| CE11                | Média maior ou igual a 3 e menor que 7 e faltas menor ou igual a 25% da carga horária |

## Casos de Teste

| CT   | Nota1 | Nota2 | Faltas | Carga Horária | Resultado Esperado   | Classe Equivalência |
| ---- | ----- | ----- | ------ | ------------- | -------------------- | ------------------- |
| CT01 | -2.00 | 8.00  | 128    | 12            | Valores Inválidos    | CE01                |
| CT02 | 12.00 | 8.00  | 128    | 12            | Valores Inválidos    | CE02                |
| CT03 | 8.00  | -2.00 | 128    | 12            | Valores Inválidos    | CE03                |
| CT04 | 8.00  | 12.00 | 128    | 12            | Valores Inválidos    | CE04                |
| CT05 | 8.00  | 8.00  | -2     | 128           | Valores Inválidos    | CE05                |
| CT06 | 8.00  | 8.00  | 130    | 128           | Valores Inválidos    | CE06                |
| CT07 | 8.00  | 8.00  | 12     | -2            | Valores Inválidos    | CE07                |
| CT08 | 8.00  | 8.00  | 12     | 128           | Aprovado.            | CE08                |
| CT09 | 8.00  | 8.00  | 33     | 128           | Reprovado por Falta. | CE09                |
| CT10 | 2.00  | 2.00  | 12     | 128           | Reprovado por Média. | CE10                |
| CT11 | 4.00  | 5.00  | 12     | 128           | Prova Extra.         | CE11                |

## Classe de teste

```java
package alfa.br.com.gilmario.teste;

import alfa.br.com.gilmario.modelo.Avaliacao;
import alfa.br.com.gilmario.modelo.ValoresInvalidosException;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class AvaliacaoTest {

    @Test
    public void testAvalia() throws ValoresInvalidosException {
        Avaliacao avaliacao = new Avaliacao();

        // Classe de Equivalência 1 - nota1 < 0
        Assertions.assertThrows(ValoresInvalidosException.class, () -> avaliacao.avalia(-2.00, 8.00, 12, 128));

        // Classe de Equivalência 2 - nota1 > 10
        Assertions.assertThrows(ValoresInvalidosException.class, () -> avaliacao.avalia(12.00, 8.00, 12, 128));

        // Classe de Equivalência 3 - nota2 < 0
        Assertions.assertThrows(ValoresInvalidosException.class, () -> avaliacao.avalia(8.00, -2.00, 12, 128));

        // Classe de Equivalência 4 - nota2 > 10
        Assertions.assertThrows(ValoresInvalidosException.class, () -> avaliacao.avalia(8.00, 12.00, 12, 128));

        // Classe de Equivalência 5 - faltas < 0
        Assertions.assertThrows(ValoresInvalidosException.class, () -> avaliacao.avalia(8.00, 8.00, -2, 128));

        // Classe de Equivalência 6 - faltas > cargaHoraria
        Assertions.assertThrows(ValoresInvalidosException.class, () -> avaliacao.avalia(8.00, 8.00, 130, 128));

        // Classe de Equivalência 7 - cargaHoraria < 0
        Assertions.assertThrows(ValoresInvalidosException.class, () -> avaliacao.avalia(8.00, 8.00, 12, -2));

        // Classe de Equivalência 8 - Aprovado
        Assertions.assertEquals("Aprovado.", avaliacao.avalia(8.00, 8.00, 12, 128));

        // Classe de Equivalência 9 - Reprovado por Falta
        Assertions.assertEquals("Reprovado por Falta.", avaliacao.avalia(8.00, 8.00, 33, 128));

        // Classe de Equivalência 10 - Reprovado por Média
        Assertions.assertEquals("Reprovado por Média.", avaliacao.avalia(2.00, 2.00, 12, 128));

        // Classe de Equivalência 11 - Prova Extra
        Assertions.assertEquals("Prova Extra.", avaliacao.avalia(4.00, 5.00, 12, 128));
    }
}
```
