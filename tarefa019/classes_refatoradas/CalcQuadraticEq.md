1. Nome de Variáveis Descritivos: As variáveis D, x1, x2 e x foram renomeadas para discriminant, root1, root2 e root, respectivamente, para tornar o código mais legível e descritivo. Usar nomes descritivos ajuda a entender o propósito de cada variável.

2. Melhorando as Mensagens de Saída: As mensagens de saída foram melhoradas para serem mais descritivas e explicativas. Agora, elas indicam quantas raízes reais existem e fornecem os valores das raízes. Isso torna a saída mais informativa.

```java
package org.example._03;

public class CalcQuadraticEq {
    public void calcQuadraticEq(double a, double b, double c) {
        double discriminant = b * b - 4 * a * c; // Mudança no nome da variável para tornar o código mais legível

        if (discriminant > 0) {
            double root1, root2; // Renomeando as variáveis para ficar mais claro
            root1 = (-b - Math.sqrt(discriminant)) / (2 * a);
            root2 = (-b + Math.sqrt(discriminant)) / (2 * a);
            System.out.println("Two distinct real roots: x1 = " + root1 + ", x2 = " + root2); // Melhorando a mensagem de saída
        } else if (discriminant == 0) {
            double root;
            root = -b / (2 * a);
            System.out.println("One real root: x = " + root); // Melhorando a mensagem de saída
        } else {
            System.out.println("No real roots exist"); // Melhorando a mensagem de saída
        }
    }
}
```
