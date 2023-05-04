## Tarefa 002 - 17/04/2022 - Pesquisa Rest API

1. Elaborar uma pesquisa sobre o tema "_Rest API_".
2. Elaborar um texto **no formato markdown** de pelo menos uma página, descrito com suas próprias palavras, destacando:
* As definições dos conceitos envolvidos;
* As principais características deste conceito (pelo menos umas cinco).

# API REST

Uma API é uma interface que permite que diferentes aplicativos de software se comuniquem entre si.  REST é um tipo de API que usa solicitações HTTP para distribuir informações e representa uma fonte de dados como uma série de recursos.  Aproveitando os recursos existentes do HTTP, como autenticação e cache, as APIs REST são simples, fáceis de usar e podem ser usadas com praticamente qualquer linguagem de programação.  As APIs REST também são escaláveis ​​e podem ser usadas para projetar aplicativos da web complexos.

Uma interface de programação de aplicativos que utiliza o design da arquitetura REST é conhecida como API RESTful.  REST (Representational State Transfer) é o estilo de arquitetura implementado no desenvolvimento de sistemas distribuídos e serviços web.  Abraçar os princípios REST é a base da API RESTful e como ela opera.  Um desenvolvedor implementando uma API REST usa uma interface de programação de aplicativos com princípios de estilo REST.

## Definições

- **API**: Uma API é uma interface de programação de aplicativos que permite a interação entre diferentes sistemas. Ela define como os sistemas podem se comunicar entre si.
- **REST**: REST é um estilo de arquitetura de software que define um conjunto de restrições para projetar serviços web. Ele permite que as aplicações acessem e manipulem informações em sistemas distribuídos usando uma interface uniforme.
- **RESTful**: Um serviço web é dito RESTful quando ele segue as restrições definidas pelo estilo arquitetural REST.

## Principais Características

A API REST é caracterizada por vários recursos principais, alguns dos quais incluem:

1. Métodos Consistentes: Para facilitar a interação entre diferentes aplicações, existe um padrão de comunicação uniforme com a API REST.  Isso consiste em métodos definidos, incluindo POST, GET, DELETE e PUT, que garantem que os recursos sejam sempre acessados ​​e manipulados de forma consistente.
2. **Stateless**: A API REST é sem estado, o que significa que não mantém nenhum estado entre as chamadas e lida com cada chamada independentemente, sem dependências de chamadas anteriores.
3. **Recursos identificáveis**: Os recursos em uma API REST têm um localizador uniforme de recursos (URL) exclusivo que pode ser usado para identificá-los.  Essa URL é composta por um caminho e um identificador de recurso exclusivo que é usado para acessar cada recurso.
4. **Formato de dados uniforme**: Usar um formato de dados uniforme é um aspecto crucial da API REST.  Ao usar JSON ou XML, os dados podem ser facilmente comunicados entre vários aplicativos, sem medo de dialeto ou plataforma.  Esse tipo de consistência permite uma comunicação fácil até mesmo entre as mais diversas aplicações.
5. **Cacheable**: A API REST pode ser armazenada em cache para diminuir a carga do servidor enquanto aprimora o desempenho.  Os clientes podem armazenar em cache as respostas da API, evitando chamadas de servidor estranhas e reutilizando os dados armazenados em cache quando necessário.  Consequentemente, nossa API pode ser armazenada em cache e pode melhorar a eficiência reduzindo as chamadas do servidor

## Conclusão

Independentemente da linguagem de programação ou plataforma usada, a API REST é uma opção popular para o desenvolvimento de serviços da web. Segue as restrições do estilo arquitetônico REST, utilizando um padrão de comunicação uniforme. Recursos identificáveis ​​por meio de uma URL exclusiva, sem estado, usando um formato de dados uniforme e podendo ser armazenados em cache também são características da API REST.