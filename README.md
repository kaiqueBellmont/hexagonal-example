## Adaptadores (Adapters):

### adapters/:

**_Nessa pasta, você tem os adaptadores que fazem a comunicação entre a sua aplicação e elementos externos, como bancos
de dados ou serviços externos_**

#### `database_adapter.py`: 
- Este é um exemplo de adaptador que se comunica com um banco de dados PostgreSQL usando
SQLAlchemy.
Ele fornece uma camada de abstração para a sua aplicação interagir com o banco de dados sem conhecer os detalhes 
específicos da implementação do banco de dados. Isso permite que você troque o banco de dados sem afetar a lógica
da aplicação.

## Portas (Ports):

### application/ports/:

**_Essa pasta contém as interfaces (portas) que definem os contratos ou contratos que sua aplicação espera que os
adaptadores implementem._**

- order_service.py: Este é um exemplo de uma porta que define um contrato para um serviço de pedidos.
Ele especifica os métodos que qualquer adaptador de serviço de pedidos deve implementar, como a criação de um pedido
ou a obtenção de um pedido.

## Domínio (Domain):

### domain/:

**_Essa pasta contém os modelos de domínio e as regras de negócio da sua aplicação. É o coração da sua aplicação e deve
ser independente de qualquer detalhe de implementação ou tecnologia_**

#### models.py: 
- Este arquivo contém a definição do modelo de domínio Order, que representa um pedido na sua aplicação.
Os modelos de domínio devem refletir as entidades principais do seu domínio e conter apenas lógica de negócios essencial.

## Application (Aplicação):

#### main.py:
- Este é o ponto de entrada da sua aplicação. É onde você configura o servidor FastAPI e define os endpoints da sua API.

#### OrderServiceAdapter:

- Este é um adaptador específico que implementa a porta `OrderService`. Ele atua como uma ponte entre os controladores
(endpoints do FastAPI) e a lógica de negócios da sua aplicação. Ele recebe solicitações dos controladores, interage com
o banco de dados por meio do adaptador de banco de dados e aplica a lógica de negócios necessária.


_Em resumo, na arquitetura hexagonal, você tem adaptadores que se comunicam com detalhes de implementação externos, 
portas que definem contratos que os adaptadores devem seguir, o domínio que contém a lógica de negócios e os modelos de
domínio, e a aplicação que usa adaptadores e portas para fornecer funcionalidade através de endpoints expostos por um
servidor FastAPI. Isso permite que você isole a lógica de negócios do restante da aplicação e facilmente substitua ou 
estenda componentes sem afetar o núcleo da sua aplicação._