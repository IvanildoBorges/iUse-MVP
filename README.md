# Sistema iUse
*A educação que circula entre todos*

<img src="docs/imagens/capa.png"/>

## Time do Projeto
- **Cicero Ivanildo Borges Alves** – Facilitador, Scrum Master, Product Owner, UX/UI Designer, Redator Geral e Desenvolvedor.
- **Maria Fernanda Sousa Silva** – Redatora, UI Designer e Desenvolvedora.
- **Yan Brasil Angelim de Brito** – Redator, UI Designer e Desenvolvedor.

## Descrição do projeto
O iUse é um sistema inspirado na **Clean Architecture**, que visa organizar o código de forma modular, separando claramente o domínio da aplicação das camadas de serviço e interface. Isso melhora a legibilidade, manutenção e testabilidade.

## Seção extensionista
### 1. Resumo e possíveis usos da nossa solução
O iUse é uma plataforma que conecta doadores e beneficiários para a doação e distribuição de materiais escolares em bom estado, com foco em pessoas em situação de vulnerabilidade social. A solução promove o reaproveitamento de recursos educacionais e pode ser utilizada por escolas, ONGs e projetos sociais para organizar campanhas de arrecadação e garantir uma distribuição mais justa e transparente. Além de facilitar doações individuais, a plataforma amplia o acesso a materiais escolares essenciais, contribuindo para a permanência e o desempenho educacional, com potencial de gerar impacto social positivo.

### 2. O que é modelagem física de dados e por que ela importa para desenvolvedores?
O projeto físico de banco de dados é a etapa em que transformamos o modelo conceitual (normalmente representado por diagramas, como o DER) em tabelas reais que podem ser criadas e utilizadas em um Sistema de Gerenciamento de Banco de Dados (SGBD), como o PostgreSQL. Nessa fase, definimos como os dados serão armazenados de fato, escolhendo tipos de dados, chaves primárias e estrangeiras, índices e regras de integridade. Essa etapa é muito importante para quem está aprendendo a programar, porque mostra como a teoria se conecta à prática. O que antes era apenas um desenho passa a ser código SQL que pode ser executado, testado e validado. Isso ajuda a entender melhor como os dados são organizados, protegidos contra inconsistências e acessados de forma eficiente. Compreender o projeto físico ajuda a desenvolver sistemas mais confiáveis, organizados e escaláveis, além de preparar o profissional para trabalhar com bancos de dados reais, como o iUse, que busca gerar impacto positivo na comunidade.

### 3. Como o design focado no usuário torna os sistemas do dia a dia melhores?
O *wireframe* atua como o esqueleto da interface, definindo a hierarquia de informações e o fluxo de ações antes da aplicação visual. Sua construção segue um processo estruturado: mapeamento das telas do MVP, seleção da ferramenta (Figma), organização da hierarquia visual, padronização de componentes e estabelecimento do fluxo de navegação. Essa etapa é crucial para validar a qualidade da interface com usuários não familiarizados, reduzindo a carga cognitiva e o tempo de aprendizado. O *design centrado no usuário (DCU)* traz em sua metodologia, a empatia como principal pilar, no qual o desenvolvedor se coloca no lugar do usuário. Por meio da utilização dessa abordagem, busca democratizar o acesso à tecnologia através da inclusão digital, da redução da carga cognitiva e da responsabilidade ética, diminuindo, assim, as barreiras de entrada para usuários, sejam eles iniciantes ou experientes.

### 4. Como o iUse funciona?
O funcionamento do sistema é simples: o doador cadastra um item informando categoria, estado de conservação e seleção do ponto de coleta (local de entrega). O beneficiário pesquisa o material disponível, realiza a reserva e recebe orientações para retirada em um ponto de coleta. Após a entrega, o sistema atualiza automaticamente o status do item e registra dados de impacto social e ecológico. Combinando arquitetura modular, usabilidade e impacto social, o iUse transforma a tecnologia em uma ferramenta prática de apoio à educação, inclusão social e reaproveitamento sustentável de recursos. Com este princípio em mente, a abordagem deixa de ser apenas técnica e passa a adotar o compromisso social como prioridade, a fim de aproximar as pessoas das soluções.

### 5. O que é Arquitetura de Software?
Lorem ipsum...

## Protótipos
Como demostração, aqui estão os dois protótipos navegáveis Figma do MVP: 
- [Mobile](https://www.figma.com/proto/9jqNWlc8OfKkiuAOGsiUQE/iUse?node-id=92-569&p=f&t=m6rzASS8Kh4UNTcv-1&scaling=scale-down&content-scaling=fixed&page-id=82%3A2&starting-point-node-id=92%3A569)
- [Desktop](https://www.figma.com/proto/9jqNWlc8OfKkiuAOGsiUQE/iUse?node-id=300-1240&p=f&t=fZ0MNb7164nYwL2X-1&scaling=scale-down&content-scaling=fixed&page-id=300%3A1239&starting-point-node-id=300%3A1240)

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
