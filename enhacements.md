Schemas: Crie esquemas (schemas) para validar dados de entrada e saída da API. Isso pode ser feito usando o Pydantic, como você já começou a fazer. Os esquemas ajudam a definir o formato esperado dos dados e a garantir que eles sejam válidos.

Repositories (Repositórios): Implemente repositórios para encapsular a lógica de acesso aos dados de persistência (banco de dados). Os repositórios são uma camada intermediária entre a lógica de aplicação e o banco de dados, e eles permitem que você troque facilmente o sistema de armazenamento subjacente sem afetar a lógica de aplicação.



Schemas (Esquemas): Os esquemas (schemas) são usados principalmente na camada de API para validar dados de entrada e saída. Eles definem a estrutura esperada dos dados que a API recebe e retorna. Os schemas não fazem parte do núcleo da arquitetura hexagonal, mas são uma parte importante para garantir a validação e a consistência dos dados que entram e saem da aplicação.

Repositories (Repositórios): Os repositórios são uma parte central da arquitetura hexagonal. Eles são usados para encapsular a lógica de acesso aos dados de persistência, como o banco de dados. Os repositórios permitem que você isole a lógica de acesso a dados do restante da aplicação, tornando-a mais flexível e desacoplada dos detalhes de armazenamento.

