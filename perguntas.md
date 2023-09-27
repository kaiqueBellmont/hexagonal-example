## Por que devo fazer a imp,ementação do repositorio completo ? "impl"

### Separação de Responsabilidades: 

- A implementação do repositório isola a lógica de acesso ao banco de dados do restante do código do aplicativo.
Isso significa que sua lógica de negócios não precisa conhecer os detalhes de como os dados são armazenados ou
recuperados. Essa separação de responsabilidades facilita a manutenção e evolução do código, pois as alterações no
sistema de armazenamento de dados não afetam diretamente a lógica de negócios.

### Testabilidade:

- Ao criar uma interface (porta) para o repositório e, em seguida, implementar uma versão concreta dessa interface
 você pode criar facilmente versões de teste do repositório que não dependem de um banco de dados real. Isso torna
os testes de unidade e de integração mais fáceis de escrever e executar, pois você pode usar implementações de
repositório simuladas ou em memória durante os testes.

### Flexibilidade:

- Se você precisar mudar a forma como os dados são armazenados (por exemplo, trocar de um banco de dados relacional
para um banco de dados NoSQL), poderá fazer isso alterando apenas a implementação do repositório, mantendo a mesma
interface. Isso permite que você adapte seu aplicativo a novos requisitos sem reescrever toda a lógica de negócios.

### Manutenção Simplificada:

- A implementação completa do repositório permite que você lide com tarefas de baixo nível relacionadas ao acesso a 
dados, como abertura de conexões com o banco de dados, execução de consultas SQL e tratamento de transações. Isso
simplifica a lógica de negócios, tornando-a mais legível e fácil de manter.

### Reutilização de Código:

- Se você tiver várias partes do aplicativo que precisam acessar os mesmos dados, pode reutilizar o mesmo repositório 
em várias partes do código, em vez de duplicar a lógica de acesso a dados.


## E os schemas? 
## Eles já fazem algo parecido com o que o models faz?

