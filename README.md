# Projeto de Matrículas

Esse projeto foi realizado para a matéria de **Projeto e Arquitetura de Software**.

## Executar projeto

O projeto requer `python` (versão igual ou acima de 3.11) e o gerenciador de pacotes `uv`.

- Rodar `uv run setup.py`, isso irá inicializar o banco de dados;
- Rodar `uv run main.py`, isso irá inicializar o servidor;
- Abrir a URL `http://localhost:8000/` no seu navegador;

## Back-end

O back-end foi desenvolvido em `python` utilizando a biblioteca `flask` para gerar endpoints REST a serem consumidos pelo front-end, e a biblioteca `peewee` para geração de classes de ORM.

O projeto do back-end segue a estrutura **MVC** para organização das camadas, com a camada de *views* possuindo o código de interface com o mundo externo, a camada *controllers* contendo a lógica de negócio da aplicação, e a camada *model* realizando a interação com o banco de dados e a modelagem das tabelas através de um **ORM**. A aplicação também usa do padrão **Observer** para a geração de logs, permitindo múltiplos destinos de logs, como para o console ou para um arquivo.

O projeto possui a seguinte organização de arquivos:

- `import.py`: Script de inicialização do banco, deve ser rodado apenas uma vez antes de iniciar a aplicação;
- `main.py`: Arquivo inicial do projeto, realiza o cadastro das *views* e dos *observers* de log;

O projeto possui a seguinte organização de pastas:

- `view/` - Pasta com as *views* da aplicação, são os endpoints que o front-end chama;
- `controller/` - Pasta com as *controllers* da aplicação, são as classes que contém toda a lógica das rotas;
- `model/`- Pasta com os modelos das entidades do banco de dados, fornecem acesso ao banco através da lib de ORM;
- `dtos/` - Pasta com modelos de *data transfer objects*, classes para uso interno de comunicação entre as camadas; 
- `loggers/` - Pasta com os *loggers*, ouvintes dos eventos de *log* para transmitir a informação. 

O processamento dos dados em CSV foi realizado com a biblioteca `pandas`, e os dados foram salvos em um banco `sqlite`.

## Front-end

O front-end foi desenvolvido em HTML, CSS e JavaScript puros, e consomem da API para mostrar os dados em tela.

O front-end utiliza o padrão do **Observer** para realizar a atualização dos dados quando algum dos inputs presentes em tela são atualizados.

A interface web dispõe dos dados em três seções:

- A primeira seção mostra a quantidade de estudantes registrados no ano selecionado, tanto em instituições públicas quando privadas;

- A segunda seção mostra o ranking de cursos, ordenado de forma decrescente pelo número de matrículas;

- A terceira seção mostra o ranking de instituições, ordenado de forma decrescente pelo número de matrículas;

Ambas tabelas respeitam os filtros específicados no topo da página, permitindo filtragem por ano, categoria administrativa da instituição e modalidade do curso;

## Desenvolvedores

- Gabriel Lovato
- Larissa
