# FastAPI Essenciais

Projeto vitrine para desenvolver APIs Rest escaláveis, seguindo as melhores práticas para performance de desenvolvimento.

## Principais Características

*   **Arquitetura Escalável**: O projeto é estruturado de forma a facilitar a escalabilidade, com uma clara separação de responsabilidades entre os diferentes módulos.
*   **Código Organizado**: A divisão em `domain`, `database`, `dependencies` e `integrations` promove um código mais limpo, coeso e de fácil manutenção.
*   **Injeção de Dependências**: Utiliza o sistema de injeção de dependências do FastAPI para gerenciar e fornecer recursos como conexões de banco de dados e autenticação.
*   **Segurança**: Inclui um módulo de segurança para autenticação e autorização, um aspecto crucial para qualquer API.

## Estrutura do Projeto

A estrutura do projeto foi pensada para ser intuitiva e facilitar o desenvolvimento:

*   `src/main.py`: Ponto de entrada da aplicação, onde a instância do FastAPI é criada e os roteadores são incluídos.
*   `src/domain/`: Contém a lógica de negócio da aplicação, dividida por domínios (ex: `admin`, `services`). Cada domínio possui seus próprios modelos, regras de negócio e rotas.
*   `src/database/`: Responsável pela comunicação com o banco de dados. Inclui a definição das tabelas (`tables.py`) e os repositórios que implementam a lógica de acesso aos dados.
*   `src/dependencies/`: Define as dependências que serão injetadas nas rotas, como a sessão do banco de dados e as verificações de segurança.
*   `src/integrations/`: Módulo dedicado a integrações com serviços externos.

## Integrações

A pasta `src/integrations` foi projetada para encapsular a lógica de comunicação com serviços de terceiros. Isso mantém o núcleo da aplicação desacoplado de detalhes de implementação de serviços externos, facilitando a manutenção e a substituição de integrações.

Atualmente, o projeto conta com uma integração de **autenticação**, que pode ser encontrada em `src/integrations/authentication`. Este módulo é responsável por:

*   Verificar credenciais de usuários.
*   Gerar e validar tokens de acesso.
*   Proteger os endpoints da API.

Esta abordagem permite que diferentes estratégias de autenticação (ex: JWT, OAuth2) possam ser adicionadas ou modificadas sem impactar o resto da aplicação.

### Detalhes Técnicos da Autenticação

A arquitetura do módulo de autenticação foi projetada para ser modular e extensível, utilizando padrões de projeto que promovem o baixo acoplamento e a alta coesão.

**Padrões Utilizados:**

*   **Strategy Pattern**: O núcleo da autenticação é baseado no padrão Strategy. A interface `BaseLoginInputStrategy` define um contrato comum para diferentes métodos de login (como email/senha, Google, etc.). Cada estratégia concreta implementa a sua própria lógica de validação no método `login()`. Isso permite adicionar novas formas de autenticação sem alterar a lógica principal do fluxo de login.

*   **Factory Pattern**: O `AuthenticationFactory` atua como uma fábrica que recebe uma estratégia de login e é responsável por orquestrar o processo. Ele utiliza a estratégia para autenticar o usuário e, se bem-sucedido, gera os tokens JWT (`access_token` e `refresh_token`). Este padrão desacopla o cliente (que solicita o login) da implementação concreta das estratégias de autenticação.

**Pontos Fortes da Arquitetura:**

*   **Extensibilidade**: Adicionar um novo provedor de autenticação (como login com Facebook ou GitHub) é simples. Basta criar uma nova classe que herde de `BaseLoginInputStrategy`, implementar a lógica de autenticação específica e registrá-la na `AuthenticationFactory`.
*   **Manutenibilidade**: Como cada estratégia de autenticação está isolada em sua própria classe, a manutenção do código é significativamente mais fácil. Alterações em uma estratégia não afetam as outras.
*   **Testabilidade**: A separação de responsabilidades facilita a criação de testes unitários para cada estratégia de autenticação de forma isolada, garantindo que cada componente funcione como esperado.
*   **Clareza e Organização**: O uso desses padrões torna o código mais claro e organizado, facilitando o entendimento do fluxo de autenticação por novos desenvolvedores.

## Como Começar

Para executar o projeto localmente, siga estes passos:

1.  **Instale as dependências:**
    ```bash
    poetry install
    ```
2.  **Execute a aplicação:**
    ```bash
    poetry run uvicorn src.main:app --reload
    ```

A API estará disponível em `http://127.0.0.1:8000`.
