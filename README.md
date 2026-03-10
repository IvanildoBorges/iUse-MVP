# Sistema iUse
*A educação que circula entre todos*

## Descrição do projeto
O iUse é um sistema inspirado na **Clean Architecture**, que visa organizar o código de forma modular, separando claramente o domínio da aplicação das camadas de serviço e interface. Isso melhora a legibilidade, manutenção e testabilidade.

## Seção extensionista
O iUse é uma plataforma que conecta doadores e beneficiários para a doação e distribuição de materiais escolares em bom estado, com foco em pessoas em situação de vulnerabilidade social. A solução promove o reaproveitamento de recursos educacionais e pode ser utilizada por escolas, ONGs e projetos sociais para organizar campanhas de arrecadação e garantir uma distribuição mais justa e transparente. Além de facilitar doações individuais, a plataforma amplia o acesso a materiais escolares essenciais, contribuindo para a permanência e o desempenho educacional, com potencial de gerar impacto social positivo.

O projeto físico de banco de dados é a etapa em que transformamos o modelo conceitual (normalmente representado por diagramas, como o DER) em tabelas reais que podem ser criadas e utilizadas em um Sistema de Gerenciamento de Banco de Dados (SGBD), como o PostgreSQL. Nessa fase, definimos como os dados serão armazenados de fato, escolhendo tipos de dados, chaves primárias e estrangeiras, índices e regras de integridade.

Essa etapa é muito importante para quem está aprendendo a programar, porque mostra como a teoria se conecta à prática. O que antes era apenas um desenho passa a ser código SQL que pode ser executado, testado e validado. Isso ajuda a entender melhor como os dados são organizados, protegidos contra inconsistências e acessados de forma eficiente.

Compreender o projeto físico ajuda a desenvolver sistemas mais confiáveis, organizados e escaláveis, além de preparar o profissional para trabalhar com bancos de dados reais, como o iUse, que busca gerar impacto positivo na comunidade.

O *wireframe* é o esqueleto da interface, é o estágio onde definimos a hierarquia das informações e o fluxo de ações do usuário.  Prototipar o wireframe é transpor para a tela os primeiros rascunhos da interface do projeto. Nesta etapa o projeto não ganha cores, mas ganha formas e estrutura. Com o wireframe é possível testar a qualidade da interface e a avaliar o fluxo de ação dos usuários que não estão familiarizados ao protótipo a fim de validar as ações principais da solução proposta.

Para sua construção, definimos algumas etapas:

-Mapear o conjunto de telas principais
-Escolher a ferramenta de prototipagem (aqui o Figma foi escolhido)
-Organizar a hierarquia visual de cada tela
-Padronizar os componentes
-Estabelecer um fluxo de navegação

Seguindo este caminho, podemos conceber o wireframe passando por todas as fases concluindo o processo ligando cada uma das telas e criando o fluxo de navegação que levará o usuário a seu objetivo final.

O *design centrado no usuário (DCU)* traz em sua metodologia, a empatia como principal pilar, no qual o desenvolvedor se coloca no lugar do usuário. Por meio da utilização dessa abordagem, busca democratizar o acesso à tecnologia através da inclusão digital, da redução da carga cognitiva e da responsabilidade ética, diminuindo, assim, as barreiras de entrada para usuários, sejam eles iniciantes ou experientes. Com este princípio em mente, a abordagem deixa de ser apenas técnica e passa a adotar o compromisso social como prioridade, a fim de aproximar as pessoas das soluções.


## Estrutura do projeto
- ```app/domain```: Contém as entidades centrais e as regras de negócio.
- ```app/services```: Serviços de aplicação, como autenticação e orquestração de fluxos.
- ```app/interfaces```: Camada de interação, com foco em **CLI** e futura integração com **API/Web**.

## Ambiente de execução e dependências
Este projeto utiliza ```Python 3``` e faz uso de um ambiente virtual ```(venv)``` para garantir o isolamento das dependências e a reprodutibilidade do ambiente de desenvolvimento.

**1. Requisitos:**
- **Python 3.10+** (recomendado)
- ```pip``` (gerenciador de pacotes do Python)

**2. Criação do ambiente virtual**
Na raiz do projeto, execute:
```bash
python -m venv venv
```

Em alguns sistemas, pode ser necessário usar:
```bash
python3 -m venv venv
```

**3. Ativação do ambiente virtual**
Windows (cmd ou PowerShell)
```bash
venv\Scripts\activate
```

Linux / macOS
```bash
source venv/bin/activate
```

*Após a ativação, o terminal exibirá ```(venv)``` indicando que o ambiente está ativo.*

*Para desativar, basta digitar no terminal*
```bash
deactivate
```

**4. Instalação das dependências**
Todas as dependências do projeto estão listadas no arquivo ```requirements.txt```.
Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

*Dependências incluídas:*
- **pytest** — framework de testes automatizados
- Outras bibliotecas necessárias ao funcionamento da aplicação

*As dependências são instaladas **exclusivamente no ambiente virtual**, não afetando o Python global do sistema.*

**5. Execução do sistema**
Com o ambiente configurado, execute:
```bash
python main.py
```

**6. Para execução dos testes**
Os testes automatizados estão localizados na pasta ```tests/``` e podem ser executados com:
```bash
pytest
```

ou mais verbosamente:

```bash
pytest -v
```

## Estrutura de pastas
```bash
iuse/
├── main.py
├── app/
│   ├── domain/
│   │   ├── models/
│   │   └── mixins/
│   ├── services/
│   ├── utils/
│   └── interfaces/
├── docs/
│   └── imagens/
└── tests/
```

## Responsabilidades por camada

- **app/domain/models**: Entidades do negócio (UML), como ```Usuario```, ```Doador```, ```Beneficiario```,  ```Item```, ```Reserva```, ```PontoColeta```, ```Entrega```, ```Retirada``` e ```Impacto```.
- **app/domain/mixins**: Comportamentos reutilizáveis, como ```AutenticavelMixin```,
- **app/services**: Regras de aplicação, incluindo **Login/Logout**, orquestração de fluxos, validações entre entidades.
- **app/interfaces**: Camada de interação com usuário (**CLI** e, no futuro, ```API / Web```)

## Fluxo de execução
O ```main.py``` atua apenas como ponto de entrada da aplicação, delegando a execução para a camada de interface. Os fluxos de uso e simulações encontram-se na camada interfaces, enquanto os testes automatizados estão isolados na pasta tests, seguindo boas práticas de arquitetura.

## Imagens da execução
Aqui estão algumas imagens que ilustram a execução do código.

**Ivanildo executando classes bases:**

**1. Tipo de Usuário (Doador/Beneficiário)**
*Descrição:* Seleção do tipo de usuário para a aplicação.

<img src="docs/imagens/tipo_De_usuarios.jpg" width="300"/>

**2. Usuário Preenchido**
*Descrição:* Tela mostrando o formulário de usuário preenchido.

<img src="docs/imagens/usuario_preenchido.jpg" width="300"/>

**3. Fim da Execução**
*Descrição:* Finalização da execução do sistema, com feedback ao usuário.

<img src="docs/imagens/fim_da_execucao.jpg" width="300"/>

**4. Testes Automatizados**
*Descrição:* Resultado da execução dos testes automatizados das classes Usuario, Doador, Beneficiario e Item.

<img src="docs/imagens/testes_da_parte_de_ivanildo.png" width="300"/>
<img src="docs/imagens/testes.jpg" width="300"/>

## Time do Projeto

- **Brenna Isabelly de Oliveira** – Facilitadora
- **Cícero Danilo do Nascimento Pereira** – Responsável pela implementação de **Retirada** e **Impacto**
- **Cícero Ivanildo Borges Alves** – Responsável pelas classes **Usuário**, **Beneficiário**, **Doador** e **Item**
- **Yan Brasil Angelim de Brito** – Responsável por **Ponto de Coleta**, **Entrega** e **Reserva**
